<div align="center">

# Lingavasan Suresh Kumar

### AI/ML Research Engineer · Software Development Engineer · Data Infrastructure · ML Systems · Open Source

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=58A6FF&center=true&vCenter=true&width=900&lines=Building+production-grade+agentic+AI%2C+data%2C+and+ML+systems;RAG+%7C+LLM+evaluation+%7C+ranking+%7C+recommendation+systems;CUDA+optimization+%7C+MLOps+%7C+cloud-native+data+infrastructure;Open-source+work+across+TensorRT%2C+ONNX+Runtime%2C+Triton%2C+Temporal%2C+and+RAJA)](https://git.io/typing-svg)

📍 Tempe, AZ &nbsp;|&nbsp; 📧 [lsuresh4@asu.edu](mailto:lsuresh4@asu.edu) &nbsp;|&nbsp; 🌐 United States

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lingavasan-suresh-kumar-50a5791aa/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Lingavasan)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lsuresh4@asu.edu)

</div>

---

## 🙋‍♂️ About

AI/ML Research and Computer Science Engineer focused on production-grade agentic AI systems, data infrastructure, and high-performance ML platforms. I build backend services, ML pipelines, RAG systems, evaluation frameworks, and cloud-native infrastructure for environments where reliability, scale, and correctness matter.

My work spans AI model development, domain-specific fine-tuning, ranking and recommendation systems, large-scale data pipelines, LLM evaluation, and performance optimization. I have worked on systems processing 8M+ daily records, maintained 99.5% uptime across production ML infrastructure, improved inference latency from 250ms to 120ms through CUDA optimization, and built agentic AI workflows achieving 95%+ precision on critical decisions.

- 🏗️ **Engineering discipline** — system design, clean interfaces, tests, CI/CD, observability, reproducibility, and maintainable code.
- 🔬 **AI systems** — LLM memory, RAG, evaluation, retrieval, ranking, fine-tuning, long-horizon behavior, and model reliability.
- 🛠️ **Production systems** — pipelines, APIs, containers, cloud infrastructure, validation gates, operational diagnostics, and model serving.
- ⚡ **Performance engineering** — CUDA kernels, C++ inference paths, GPU memory optimization, profiling, and low-latency serving.
- 🤝 **Open-source mindset** — practical fixes, regression coverage, runtime tooling, SDK improvements, and documentation that helps maintainers.

### Engineering Principles

| Focus | Practice |
|---|---|
| Clear problem framing | Understand constraints, define expected behavior, and make tradeoffs explicit |
| Maintainable systems | Prefer reusable pipelines, typed interfaces, versioned data, and automation |
| Reliability | Use tests, validation gates, observability, and reproducible workflows |
| Communication | Translate technical details into decisions, risks, and next steps |
| Code quality | Keep changes reviewable, documented, and easy to extend |

---

## 🚀 Recent Open Source

Recent public work across ML infrastructure, runtime tooling, SDKs, and HPC documentation.

| Project | What I Contributed |
|---|---|
| [NVIDIA/TensorRT#4779](https://github.com/NVIDIA/TensorRT/pull/4779) | Fixed Polygraphy `data to-input` multi-iteration aliasing so each padded input iteration keeps distinct values, with regression coverage for the affected path. |
| [microsoft/onnxruntime#28534](https://github.com/microsoft/onnxruntime/pull/28534) | Added WebGPU `ProgramBase` reserve helpers and capacity hints for inputs, outputs, and uniforms to reduce vector reallocations in convolution setup paths. |
| [triton-lang/triton#10425](https://github.com/triton-lang/triton/pull/10425) | Disabled autotune disk caching when custom `do_bench` functions or deprecated benchmark knobs change benchmark behavior, with focused runtime/autotuner coverage. |
| [temporalio/sdk-python#1556](https://github.com/temporalio/sdk-python/pull/1556) | Exposed a public `JSONTypeConverterUnhandled` sentinel type, preserved compatibility aliasing, and updated converter tests/docs. |
| [llnl/RAJA#2032](https://github.com/llnl/RAJA/pull/2032) | Documented reducer helper utilities, including `accumulate`, `binary_tree_reduce`, `high_accuracy_reduce`, and Kahan-sum helper types/functions, then validated the generated Sphinx docs. |

> Open source is where I practice careful engineering in public: focused fixes, performance work, tests, and documentation that make projects easier to use and maintain.

---

## 🎯 Engineering Focus

My work sits across a few connected areas:

| Area | Strengths |
|---|---|
| **Software Development Engineer** | Backend services, APIs, system design, microservices, testing, CI/CD, code quality, and production ownership |
| **AI / LLM Engineer** | RAG, agentic workflows, prompt/context systems, SFT/RLHF workflows, model evaluation, fine-tuning, and hallucination reduction |
| **ML Infrastructure Engineer** | Model serving, feature pipelines, MLflow, A/B testing, model monitoring, evaluation harnesses, and MLOps workflows |
| **Data Infrastructure Engineer** | Airflow, Spark, Databricks, dbt, Snowflake, BigQuery, Redshift, ETL/ELT, data modeling, and warehouse optimization |
| **ML Acceleration Engineer** | CUDA kernels, GPU memory optimization, C++ inference paths, TensorRT/ONNX Runtime work, profiling, and latency reduction |
| **Research / AI Systems** | Memory governance, adversarial robustness, long-horizon agents, evaluation methodology, reproducibility, and publications |

---

## 💼 Experience

### Software Development Engineer - AI/ML — Perpendo AI, United States
**Jun 2026 – Present**

Building production-grade agentic AI systems for regulated insurance workflows, with an emphasis on reliability, grounded reasoning, observability, and deployment-ready backend integrations.

**Key Contributions**
- 🧠 **Agentic AI workflows** — Designed multi-step reasoning, tool-use patterns, and orchestration logic for regulated insurance processes, achieving 95%+ precision on critical decisions.
- ☁️ **Production deployment** — Architected AWS deployment infrastructure using Amazon EKS and backend API integrations for reliable production traffic.
- 📚 **Hybrid RAG systems** — Grounded AI reasoning in insurance-specific knowledge sources including policy language, regulatory guidance, and underwriting criteria, improving output accuracy to 96% and reducing ungrounded responses by 38%.
- 🔎 **Observability** — Built distributed tracing across LLM pipelines and agentic workflows, improving error detection and issue resolution by 67%.
- 🧪 **Evaluation systems** — Built benchmarking suites against insurance-domain quality standards across precision, consistency, defensibility, latency, cost, and tool-use performance.
- 🔁 **Self-correction loops** — Designed self-reflective correction mechanisms with human-in-the-loop synchronization, reducing system failure rate by 88%.

`Python` `FastAPI` `AWS` `Amazon EKS` `Agentic AI` `RAG` `LangChain` `LangGraph` `OpenTelemetry` `LLM Evaluation` `MLOps` `CI/CD`

---

### Graduate Researcher — Arizona State University, Tempe, AZ
**Jul 2025 – Present**

Researching memory governance, hallucination resistance, adversarial robustness, and reliable autonomous AI systems.

**Key Contributions**
- 🔬 **Memory governance** — Designed policy-driven memory governance middleware for autonomous AI agents, achieving 83.3% accuracy versus a 78% baseline on long-context memory tasks.
- 🛡️ **Robustness testing** — Built evaluation infrastructure against adversarial memory-poisoning attacks, including MINJA, PoisonedRAG, and AgentPoison attack vectors.
- 📉 **Token efficiency** — Reduced token usage by 47% while improving hallucination resistance, transparency, and performance stability across persistent, multi-session, multi-agent LLM systems.
- 🧭 **Retrieval policy** — Designed intent-aware, semantically ranked retrieval heuristics and declarative policies for memory retention, retrieval, and abstraction.
- 📄 **Research output** — Published [MemArchitect: A Policy Driven Memory Governance Layer](https://arxiv.org/abs/2603.18330) on arXiv.

`Python` `LangChain` `LangGraph` `RAG` `Pinecone` `LanceDB` `OpenAI APIs` `Hugging Face` `MLflow` `Evaluation Frameworks`

---

### Software Development Engineer - Data Infrastructure — Arizona State University, Tempe, AZ
**Nov 2024 – Jun 2026**

Built data reliability, cloud infrastructure, and operational tooling for distributed research workflows where correctness, access control, and repeatability matter.

**Key Contributions**
- 🏗️ **Cloud-native services** — Architected scalable Python microservices on AWS for distributed ingestion and processing across concurrent research pipelines.
- 🚦 **Operational diagnostics** — Developed multithreaded C++ and Python services for workflow diagnostics and failure detection, reducing incident triage time by 60%.
- 🗄️ **Data modeling** — Designed relational data models and integrity enforcement mechanisms in PostgreSQL, using indexing and foreign key strategies to optimize query performance by 3x.
- ✅ **Reliable pipelines** — Collaborated across engineering teams to optimize data pipelines for throughput, reliability, and fault tolerance, ensuring 99.9% uptime for critical workflows.
- 🧪 **Research infrastructure** — Built validation frameworks, measurement systems, and benchmark datasets used across 3+ ML research projects.

`Python` `C++` `SQL` `FastAPI` `AWS` `PostgreSQL` `Airflow` `dbt` `Great Expectations` `Docker` `CI/CD` `PyTest` `IAM` `OAuth`

---

### Assistant Content & SEO Manager — Sportskeeda
**Dec 2023 – Jul 2024**

Led content operations, analytics, forecasting, automation, and reporting workflows supporting editorial and product decisions.

**Key Contributions**
- 📊 **Team leadership** — Led a global team of 40+ members across editorial, content operations, and analytics, including hiring, performance reviews, and team development.
- 📈 **SEO analytics** — Owned product analytics for SEO features, driving 54x organic traffic growth through systematic keyword optimization and engagement experimentation.
- 📉 **Forecasting** — Designed time-series forecasting models in Python/R to predict content traffic and revenue for quarterly planning.
- 🧰 **Dashboards** — Built Power BI and Looker dashboards tracking content KPIs, engagement metrics, and revenue performance across 40+ team workflows.
- ⚙️ **Automation** — Automated SEO scoring and content optimization using Python and NLP techniques, reducing manual work by 40%.

`Python` `SQL` `Pandas` `NumPy` `SciPy` `Power BI` `Looker` `Google Analytics` `D3.js` `Forecasting` `NLP`

---

### AI Engineer — Scale AI
**Oct 2023 – Jan 2024**

Worked on domain-specific prompt design, LLM evaluation, feedback workflows, and inference-efficiency assessment.

**Key Contributions**
- 🧩 **Prompt systems** — Designed 350+ domain-specific prompts utilizing Supervised Fine-Tuning (SFT) and RLHF workflows to improve large language model reasoning and objective alignment.
- 🔁 **Evaluation pipelines** — Built CI/CD-integrated prompt-quality assessment workflows, enabling 25% faster iteration cycles for model improvement.
- 🧠 **Structured feedback** — Delivered feedback mechanisms that increased model accuracy by 12% and reduced hallucination rates by 30% across evaluated outputs.
- ⚙️ **Inference analysis** — Evaluated deep learning model inference efficiency across scenarios and assessed tokenization impact on model performance and computational requirements.

`Prompt Engineering` `SFT` `RLHF` `LLM Evaluation` `Inference Analysis` `Python` `Prompt Quality` `Model Alignment`

---

### Software Development Engineer - Machine Learning — DevelUp, Bangalore
**Sep 2021 – Nov 2023**

Joined as a founding engineer to build and scale the AI/ML layer of an early-stage job-matching platform from data ingestion through production inference.

**Key Contributions**
- 🏁 **Founding engineering** — Designed and scaled end-to-end ML systems serving 8M+ daily records across ingestion, training data generation, model deployment, and production inference.
- 🚀 **Production ML ownership** — Operated 25+ production models, maintained 99.5% uptime, and served 250K+ daily inference requests at 120ms average latency.
- ⚡ **CUDA optimization** — Reduced inference latency from 250ms to 120ms through NVIDIA profiling and CUDA kernel optimization, while reducing GPU memory footprint by 30%.
- 🔍 **Ranking and retrieval** — Built and fine-tuned transformer-based retrieval models for job-candidate matching, improving search relevance by 20% through offline evaluation and online A/B testing.
- 🗄️ **Warehouse optimization** — Designed dimensional data models and optimized SQL query performance from 45 seconds to 3 seconds through schema and index optimization.
- 🔄 **ML pipelines** — Architected Airflow-orchestrated Spark and Delta Lake pipelines on Databricks, processing 8M+ daily records in Parquet format into Snowflake-backed analytics and training datasets.
- 🐳 **Production services** — Containerized scalable Python microservices using Docker and Kubernetes with GitHub Actions CI/CD, integrating OpenAI and LLM inference pipelines with backend APIs.

`Python` `C++` `CUDA` `PyTorch` `TensorFlow` `Keras` `scikit-learn` `XGBoost` `BERT` `LangChain` `RAG` `LanceDB` `Pinecone` `FastAPI` `Spark` `Databricks` `Snowflake` `Docker` `Kubernetes` `MLflow`

---

## 🔬 Research

### MemArchitect: Policy Driven Memory Governance for LLM Agent Systems
**Arizona State University · arXiv:2603.18330**

> Long-running agents do not just need more context. They need governed memory: what gets stored, what expires, what is allowed back into the prompt, how contradictions are resolved, and how token budgets are spent.

**MemArchitect** is a model-agnostic external memory governance layer for persistent LLM agents. It treats memory as a constrained, auditable resource rather than a passive transcript or naive similarity-search log.

| Governance Stage | What It Controls |
|---|---|
| **Write policy** | Filters noise, duplicates, injection attempts, and low-value traces before storage |
| **Metadata & provenance** | Tracks source, time scope, trust, sensitivity, and retrieval eligibility |
| **TTL / decay** | Applies configurable forgetting behavior by memory type |
| **Consolidation** | Compresses episodic traces into compact semantic summaries |
| **Contradiction handling** | Flags conflicting facts before they reach the model context |
| **Token budget arbitration** | Selects useful memories under hard context-window limits |
| **Compliance layer** | Supports deletion cascades and "do not store" style policies |

`Python` `LangChain` `LangGraph` `RAG` `Pinecone` `LanceDB` `OpenAI APIs` `Hugging Face` `Evaluation` `MLflow`

---

## 📄 Publications

### [MemArchitect: A Policy Driven Memory Governance Layer](https://arxiv.org/abs/2603.18330)

**arXiv · March 2026**

Introduced a policy-driven memory governance layer for persistent LLM agents, covering memory lifecycle management, conflict resolution, privacy controls, decay, retrieval governance, hallucination resistance, and structured evaluation for reliable autonomous systems.

`LLM Agents` `Memory Governance` `RAG` `Agentic AI` `Adversarial Robustness` `Evaluation Frameworks`

### [Multimodal AI-Based Workload Relocation Strategy for Reducing Carbon Emissions in Multi-Cloud Environments](https://ieeexplore.ieee.org/document/11379581)

**IEEE Xplore · ICECONF 2025**

[DOI: 10.1109/ICECONF65644.2025.11379581](https://doi.org/10.1109/ICECONF65644.2025.11379581)

Co-authored a carbon-aware workload relocation framework for multi-cloud environments using reinforcement learning, forecasting, and constraint-aware optimization to balance cost, performance, energy efficiency, and emissions.

`Ray RLlib` `PyTorch` `Hugging Face Transformers` `LSTM` `Carbon-Aware Scheduling` `Energy Modeling` `Pandas` `Python`

---

## 🛠️ Technical Skills

### 🐍 Backend & Core Programming
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

Python · SQL · Java · C/C++ · Go · TypeScript · FastAPI · RESTful APIs · Microservices · System Design · OOP Design · Design Patterns · API Contract Design · Event-Driven Architecture · PyTest · Unit/Integration Testing

---

### 🤖 AI, ML & LLM Systems
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![ONNX](https://img.shields.io/badge/ONNX-005CED?style=for-the-badge&logo=onnx&logoColor=white)

PyTorch · TensorFlow · Keras · scikit-learn · XGBoost · Transformers · BERT Fine-Tuning · Ranking Systems · Recommendation Systems · RAG · LangChain · LangGraph · LanceDB · Pinecone · OpenAI APIs · Anthropic APIs · SFT/RLHF Workflows · Prompt/Context Management · Agentic Workflow Design · LLM Evaluation · Model Alignment

---

### 📊 Data Engineering & Warehousing
![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

Apache Airflow · Apache Spark · Databricks · Delta Lake · dbt · ETL/ELT Pipeline Design · Batch/Streaming Processing · PostgreSQL · MySQL · Snowflake · Google BigQuery · Amazon Redshift · Data Warehouse Architecture · Dimensional/Star Schema Design · 3NF Modeling · Query Optimization · Indexing Strategies · Parquet

---

### ☁️ Cloud Infrastructure & MLOps
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)

AWS S3 · AWS Lambda · Amazon SageMaker · Amazon Redshift · EC2 · Amazon EKS · Google BigQuery · Dataflow · Composer · Dataproc · Pub/Sub · Azure Blob Storage · Azure Functions · Azure Machine Learning · Synapse Analytics · Azure Databricks · AKS · Docker · Kubernetes · GitHub Actions · CI/CD · MLflow · Model Deployment & Serving · Feature Engineering Pipelines · A/B Testing · Model Monitoring

---

### ⚡ Performance, Reliability & Observability
![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=for-the-badge&logo=opentelemetry&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

CUDA Kernel Optimization · NVIDIA Profiling · ONNX Runtime · TensorRT / Polygraphy · Inference Latency Optimization · GPU Memory Optimization · Query Tuning · Performance Profiling · Great Expectations · Data Validation Frameworks · Automated Quality Checks · OpenTelemetry · Distributed Tracing · Structured Logging · SLO/Error Budget Tracking · Fault-Tolerant System Design · OAuth · SAML · IAM

---

## 🏆 Leadership & Professional Activities

- 📝 **ICLR 2026 Reviewer** — technical review experience across modern AI research, evaluation methodology, and reliable ML systems.
- 🌱 **Published researcher** — memory governance for autonomous AI systems and carbon-aware multi-cloud workload relocation.
- 🤝 **Open-source contributor** — practical fixes, performance improvements, regression coverage, and documentation across production-grade repositories.
- 🌐 **Cross-functional builder** — experience translating technical systems into decisions, risks, implementation plans, and measurable product outcomes.

---

## 📊 GitHub Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Lingavasan&show_icons=true&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true" height="165" />
&nbsp;&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Lingavasan&layout=compact&theme=github_dark&hide_border=true" height="165" />

</div>

<div align="center">

[![GitHub Streak](https://streak-stats.demolab.com?user=Lingavasan&theme=github-dark-blue&hide_border=true)](https://git.io/streak-stats)

</div>

---

## ⚙️ How I Work

> I build with production constraints in mind: correctness, latency, cost, infrastructure, observability, and maintainability.
> I treat tests, documentation, and clear ownership as part of the product.
> I write code and research artifacts with the next engineer, reviewer, or maintainer in mind.

---

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=Lingavasan&color=58A6FF&style=flat-square&label=Profile+Views)

</div>
