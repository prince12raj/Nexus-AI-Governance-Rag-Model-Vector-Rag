```python
import gradio as gr
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


# =========================
# Load RAG resources
# =========================

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

index = faiss.read_index("data/vector_db/gdpr.index")

metadata = pd.read_csv(
    "data/vector_db/gdpr_metadata.csv"
)


# =========================
# Compliance rules
# =========================

compliance_rules = {
    "Data Retention": [
        "retain personal data indefinitely",
        "delete old customer records",
        "retention period",
        "storage limitation",
        "delete personal data",
        "erase personal data",
        "keep data indefinitely"
    ],

    "Data Collection": [
        "collect personal data",
        "necessary personal data",
        "purpose of collection",
        "data minimization",
        "minimum data"
    ],

    "Data Security": [
        "protect personal data",
        "security measures",
        "unauthorized access",
        "encryption",
        "security"
    ]
}


# =========================
# Detect compliance areas
# =========================

def detect_compliance_area(policy):

    policy_lower = policy.lower()

    areas = []

    for area, keywords in compliance_rules.items():

        for keyword in keywords:

            if keyword.lower() in policy_lower:
                areas.append(area)
                break

    return areas


# =========================
# Retrieve relevant evidence
# =========================

def retrieve(query, k=5):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for rank, idx in enumerate(indices[0]):

        if idx == -1:
            continue

        row = metadata.iloc[idx]

        results.append({
            "rank": rank + 1,
            "distance": float(distances[0][rank]),
            "record_id": row["clause_id"],
            "chunk_id": row["chunk_id"],
            "text": row["text"]
        })

    return results


# =========================
# Calculate risk score
# =========================

def calculate_score(areas):

    score = 100

    if "Data Retention" in areas:
        score -= 40

    if "Data Collection" in areas:
        score -= 20

    if "Data Security" in areas:
        score -= 20

    return max(score, 0)


# =========================
# Recommendations
# =========================

def generate_recommendations(areas):

    recommendations = []

    if "Data Retention" in areas:

        recommendations.append(
            "Define a clear data retention period and delete or anonymize personal data when it is no longer required."
        )

    if "Data Collection" in areas:

        recommendations.append(
            "Collect only personal data that is necessary for the stated purpose."
        )

    if "Data Security" in areas:

        recommendations.append(
            "Implement appropriate technical and organizational security measures to protect personal data."
        )

    if not recommendations:

        recommendations.append(
            "Review the policy against the available GDPR evidence."
        )

    return recommendations


# =========================
# Main audit function
# =========================

def run_audit(policy):

    if not policy.strip():

        return (
            "Please enter a company policy.",
            "",
            "",
            ""
        )

    areas = detect_compliance_area(policy)

    results = retrieve(policy, k=5)

    score = calculate_score(areas)

    recommendations = generate_recommendations(areas)


    # Verdict

    if not results:

        verdict = "INSUFFICIENT EVIDENCE"

    elif "Data Retention" in areas:

        verdict = "REVIEW REQUIRED"

    else:

        verdict = "REVIEW REQUIRED"


    # Risk

    if score < 70:

        risk = "HIGH"

    elif score < 90:

        risk = "MEDIUM"

    else:

        risk = "LOW"


    # Summary

    summary = f"""
## Compliance Audit Result

**Verdict:** {verdict}

**Risk Level:** {risk}

**Nexus Compliance Risk Score:** {score}/100

**Detected Compliance Areas:**
{", ".join(areas) if areas else "No specific area detected"}
"""


    # Evidence

    evidence_text = ""

    for result in results:

        evidence_text += f"""
### Evidence {result['rank']}

**Record ID:** {result['record_id']}

**Chunk ID:** {result['chunk_id']}

**Similarity Distance:** {result['distance']:.4f}

{result['text']}

---
"""


    # Recommendations

    recommendation_text = ""

    for recommendation in recommendations:

        recommendation_text += f"- {recommendation}\n"


    return (
        summary,
        evidence_text,
        recommendation_text,
        f"Retrieved {len(results)} relevant evidence records."
    )


# =========================
# Gradio Interface
# =========================

with gr.Blocks(
    title="Nexus AI Governance"
) as demo:

    gr.Markdown(
        """
# 🛡️ Nexus AI Governance Platform

### RAG-Based Compliance Audit System

Enter a company policy below to retrieve relevant GDPR evidence
and identify potential compliance risks.
"""
    )


    policy_input = gr.Textbox(
        label="Company Policy",
        placeholder=(
            "Example: Our company retains all customer personal "
            "data indefinitely and does not automatically delete "
            "old customer records."
        ),
        lines=8
    )


    audit_button = gr.Button(
        "🔍 Run Compliance Audit",
        variant="primary"
    )


    summary_output = gr.Markdown(
        label="Audit Result"
    )

    evidence_output = gr.Markdown(
        label="Retrieved Evidence"
    )

    recommendation_output = gr.Markdown(
        label="Recommendations"
    )

    status_output = gr.Markdown()


    audit_button.click(
        fn=run_audit,
        inputs=policy_input,
        outputs=[
            summary_output,
            evidence_output,
            recommendation_output,
            status_output
        ]
    )


    gr.Markdown(
        """
---

**Note:** This system provides automated compliance-risk analysis
based on the available GDPR dataset. It is not legal advice and the
score is a project-specific risk indicator, not an official GDPR
compliance score.
"""
    )


if __name__ == "__main__":
    demo.launch()
```
