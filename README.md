<div align="center">

# 🛡️ NEXUS AI GOVERNANCE

### Intelligent Compliance • Regulatory Intelligence • AI Governance

**A RAG-based compliance audit platform that connects organizational policies with regulatory evidence using semantic search and vector retrieval.**

<br>

[![Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-00C853?style=for-the-badge)](https://nexus-ai-governance-0007.streamlit.app/)
[![Hugging Face](https://img.shields.io/badge/🤗_HUGGING_FACE-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/prince12raj/nexus-ai-governance)
[![GitHub](https://img.shields.io/badge/💻_SOURCE_CODE-181717?style=for-the-badge\&logo=github)](https://github.com/prince12raj/nexus-ai-governance)

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square\&logo=python\&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-00A98F?style=flat-square)
![Sentence Transformers](https://img.shields.io/badge/Sentence_Transformers-Embeddings-FF6F00?style=flat-square)
![Gradio](https://img.shields.io/badge/Gradio-UI-FF4B4B?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=flat-square)
![GDPR](https://img.shields.io/badge/Framework-GDPR-4285F4?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-2EA44F?style=flat-square)

</div>

---

## 🚀 Live Demo

| Platform                  | Link                                                                                     |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| 🌐 **Web Application**    | [Launch Nexus AI Governance](https://nexus-ai-governance-0007.streamlit.app/)            |
| 🤗 **Hugging Face Space** | [Open Hugging Face Space](https://huggingface.co/spaces/prince12raj/nexus-ai-governance) |
| 💻 **GitHub Repository**  | [View Source Code](https://github.com/prince12raj/nexus-ai-governance)                   |

---

# 🧭 What is Nexus?

**Nexus AI Governance** is a compliance intelligence platform designed to analyze organizational policies against regulatory knowledge.

Instead of manually searching through large regulatory documents, Nexus uses:

> **Text Processing → Semantic Embeddings → Vector Search → Evidence Retrieval → Compliance Analysis → Risk Assessment**

The current prototype focuses on **GDPR-related compliance analysis** using a retrieval pipeline built with **Sentence Transformers and FAISS**, followed by a rule-based compliance engine.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────────┐
                    │   🏢 ORGANIZATIONAL      │
                    │        POLICY            │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │    Text Processing       │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │  Sentence Transformer   │
                    │    all-MiniLM-L6-v2      │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │      Vector Query        │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │     FAISS Index          │
                    │    Semantic Search       │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   📚 Relevant Evidence   │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Compliance Engine      │
                    └────────────┬─────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
        Data Retention     Data Collection     Data Security
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 ▼
                    ┌──────────────────────────┐
                    │      📊 Risk Analysis    │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │    💡 Recommendations    │
                    └──────────────────────────┘
```

---

# ✨ Core Features

| Feature                     | Description                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------- |
| 🔎 **Semantic Search**      | Finds regulatory evidence based on semantic meaning rather than simple keyword matching. |
| 🧠 **RAG Pipeline**         | Retrieves relevant regulatory information from an indexed knowledge base.                |
| 📚 **Evidence Retrieval**   | Displays the evidence used during policy analysis.                                       |
| 🛡️ **Compliance Analysis** | Detects potential compliance issues across supported areas.                              |
| 📊 **Risk Assessment**      | Generates a project-specific risk indicator.                                             |
| 💡 **Recommendations**      | Provides suggestions based on detected compliance concerns.                              |
| 🌐 **Web Interface**        | Provides an interactive interface for policy analysis.                                   |
| ☁️ **Cloud Deployment**     | Available through Streamlit and Hugging Face Spaces.                                     |

---

# 🎯 Problem Statement

Organizations have to deal with large amounts of:

* Internal policies
* Regulatory requirements
* Privacy requirements
* Security standards
* Compliance documentation

Traditional compliance review can require analysts to repeatedly perform:

```text
Read
  ↓
Search
  ↓
Compare
  ↓
Interpret
  ↓
Document
```

This process can become time-consuming as the number of policies and regulations increases.

### Nexus Workflow

```text
             INPUT POLICY
                  │
                  ▼
         ┌─────────────────┐
         │ Semantic Search │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Relevant GDPR   │
         │    Evidence     │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Compliance      │
         │ Analysis        │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Risk Detection  │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Recommendations │
         └─────────────────┘
```

---

# 🧠 RAG Pipeline

The retrieval pipeline consists of the following stages:

```text
┌─────────────────────────┐
│   GDPR Dataset          │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Data Processing       │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Text Chunking         │
│   150 words / 30 overlap│
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Sentence Embeddings   │
│   all-MiniLM-L6-v2      │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   FAISS Vector Index    │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Top-K Retrieval       │
│   K = 5                 │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Compliance Engine     │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Risk + Recommendations│
└─────────────────────────┘
```

---

# 🔬 Current Compliance Areas

### 🗃️ Data Retention

The system detects policies related to:

* Indefinite personal-data retention
* Retention periods
* Data deletion
* Data erasure
* Storage limitation

---

### 📥 Data Collection

The system analyzes concepts such as:

* Personal data collection
* Data minimization
* Purpose of collection
* Collection of unnecessary information

---

### 🔐 Data Security

The system detects concepts related to:

* Unauthorized access
* Security measures
* Data protection
* Encryption

---

# 📊 Example Audit

### Input Policy

```text
Our company retains all customer personal data indefinitely
and does not automatically delete old customer records.
```

### Nexus Output

```text
╔══════════════════════════════════════╗
║          COMPLIANCE AUDIT            ║
╠══════════════════════════════════════╣
║                                      ║
║  Verdict     : REVIEW REQUIRED       ║
║  Risk Level  : HIGH                  ║
║  Score       : 60 / 100              ║
║  Area        : Data Retention        ║
║                                      ║
╚══════════════════════════════════════╝
```

### 💡 Recommendation

> Define a clear data-retention period and delete or anonymize personal data when it is no longer required.

---

# 🛠️ Technology Stack

| Layer                   | Technology                |
| ----------------------- | ------------------------- |
| 🐍 Programming Language | **Python**                |
| 🧠 Embeddings           | **Sentence Transformers** |
| 🤖 Embedding Model      | **all-MiniLM-L6-v2**      |
| ⚡ Vector Database       | **FAISS**                 |
| 📊 Data Processing      | **Pandas + NumPy**        |
| 🎨 Interface            | **Gradio**                |
| 🌐 Web Application      | **Streamlit**             |
| ☁️ Deployment           | **Hugging Face Spaces**   |
| 📜 Compliance Framework | **GDPR**                  |

---

# 📂 Project Structure

```text
nexus-ai-governance/
│
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 README.md
│
├── 📁 data/
│   │
│   ├── 📁 raw/
│   │
│   ├── 📁 processed/
│   │   ├── gdpr_raw.csv
│   │   ├── gdpr_regulations.csv
│   │   └── gdpr_rag_chunks.csv
│   │
│   └── 📁 vector_db/
│       ├── gdpr.index
│       └── gdpr_metadata.csv
│
└── 📓 nexus_rag_prototype.ipynb
```

---

# ⚙️ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/prince12raj/nexus-ai-governance.git
cd nexus-ai-governance
```

### 2️⃣ Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
python app.py
```

---

# 📦 Requirements

```text
gradio
pandas
numpy
faiss-cpu
sentence-transformers
torch
```

---

# 🔐 Privacy & Security

The current prototype does **not** require:

```text
❌ OpenAI API
❌ Ollama
❌ External LLM APIs
```

The core pipeline uses:

```text
Local Embedding Model
        +
FAISS Vector Database
        +
Regulatory Metadata
        +
Rule-Based Compliance Engine
```

For production environments, additional controls would be required before processing confidential organizational information.

---

# 🚧 Project Status

| Component                 | Status |
| ------------------------- | :----: |
| GDPR Knowledge Base       |    ✅   |
| Data Processing           |    ✅   |
| Text Chunking             |    ✅   |
| Embeddings                |    ✅   |
| FAISS Retrieval           |    ✅   |
| Semantic Search           |    ✅   |
| Compliance Detection      |    ✅   |
| Risk Assessment           |    ✅   |
| Recommendations           |    ✅   |
| Streamlit Web Application |    ✅   |
| Hugging Face Deployment   |   🚀   |
| Multi-Framework Support   |   🔜   |
| LLM Reasoning             |   🔜   |

---

# 🔮 Roadmap

### 🌍 Multi-Framework Compliance

```text
              GDPR
                │
                ▼
           ISO 27001
                │
                ▼
              HIPAA
                │
                ▼
              SOC 2
                │
                ▼
            PCI-DSS
```

### 🤖 Advanced AI

* LLM-powered compliance reasoning
* Explainable AI
* Policy-to-regulation traceability
* Natural-language audit reports
* Multi-agent compliance auditing

### 🏢 Enterprise Features

* PDF/document ingestion
* PII detection
* Prompt-injection protection
* Role-based access control
* Compliance dashboards
* Audit history
* Regulatory knowledge updates
* Organization-specific knowledge bases

---

# 🧩 Key Concepts Demonstrated

```text
                    NEXUS
                      │
          ┌───────────┴───────────┐
          │                       │
         RAG               Compliance
          │                       │
    ┌─────┼─────┐          ┌──────┼──────┐
    │     │     │          │      │      │
Embedding FAISS Search    Risk  Evidence Rules
    │     │     │          │      │      │
    └─────┴─────┘          └──────┴──────┘
```

### Technical Concepts

* Retrieval-Augmented Generation architecture
* Semantic embeddings
* Vector similarity search
* FAISS indexing
* Text chunking
* Regulatory knowledge retrieval
* Rule-based compliance detection
* Risk analysis
* Recommendation generation

---

# 📈 Why Nexus?

Nexus demonstrates how modern AI engineering and information-retrieval techniques can be applied to a practical governance and compliance problem.

The project combines:

**AI / ML**

→ Semantic embeddings
→ Vector search
→ Retrieval pipelines

**Software Engineering**

→ Python
→ Data processing
→ Web application
→ Cloud deployment

**Governance**

→ GDPR knowledge
→ Compliance analysis
→ Risk identification
→ Evidence-based recommendations

---

# 👨‍💻 Developer

<div align="center">

## Prince Raj

**B.Tech Computer Science & Engineering**

[![GitHub](https://img.shields.io/badge/GitHub-prince12raj-181717?style=for-the-badge\&logo=github)](https://github.com/prince12raj)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Prince_Raj-0A66C2?style=for-the-badge\&logo=linkedin)](https://www.linkedin.com/in/prince-raj-1a1801309/)

</div>

---

# 🌐 Project Links

### 🚀 Live Application

**[Launch Nexus AI Governance →](https://nexus-ai-governance-0007.streamlit.app/)**

### 🤗 Hugging Face

**[Open Nexus AI Governance Space →](https://huggingface.co/spaces/prince12raj/nexus-ai-governance)**

### 💻 GitHub

**[View Nexus AI Governance Repository →](https://github.com/prince12raj/nexus-ai-governance)**

---

# ⚠️ Disclaimer

Nexus AI Governance is an **educational and research project**.

The system provides automated compliance-risk analysis based on its available knowledge base. It does **not** provide legal advice, certify regulatory compliance, or replace qualified legal and compliance professionals.

The risk score displayed by the application is a **project-specific risk indicator**, not an official GDPR compliance score.

---

<div align="center">

# 🛡️ NEXUS AI GOVERNANCE

### *Connect Policies. Retrieve Evidence. Identify Risk.*

<br>

⭐ **If you find this project interesting, consider starring the repository.**

</div>
