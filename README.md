<div align="center">

# Lingavasan Suresh Kumar

### Data Engineer · AI/ML Engineer · LLM Systems · Applied Research

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=58A6FF&center=true&vCenter=true&width=700&lines=Building+reliable+data+systems+%26+production-grade+AI;Agent+memory+%7C+optimization+%7C+multi-cloud+sustainability;Engineering+discipline+meets+research+curiosity)](https://git.io/typing-svg)

📍 Tempe, AZ &nbsp;|&nbsp; 📞 +1 (480) 819-2073 &nbsp;|&nbsp; 📧 [lsuresh4@asu.edu](mailto:lsuresh4@asu.edu)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/linga-vasan-50a5791aa)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Lingavasan)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lsuresh4@asu.edu)

</div>

---

## 🙋‍♂️ About

I build reliable data systems and production-grade AI that hold up when the environment is messy: incomplete inputs, shifting requirements, compute budgets, latency targets, and stakeholders who need clarity—not complexity.

My identity is shaped by two instincts:

- 🏗️ **Engineering discipline** — data contracts, observability, quality gates, reproducibility, secure-by-default architecture.
- 🔬 **Research curiosity** — building systems that learn, reason, adapt; especially agentic LLM behavior, long-horizon workflows, and memory under constraints.

I operate like a manager even when the title isn't explicit: I translate ambiguity into a plan, build alignment, define success metrics, unblock teams, and deliver outcomes with clean technical ownership.

### What I'm optimizing for

| Focus | Practice |
|---|---|
| Clarity before execution | Problem definition, constraints, success metrics, decision boundaries |
| Systems that scale | Reusable pipelines, versioned data, automation over one-off scripts |
| Operational excellence | Observability, incident playbooks, failure-mode thinking, QA |
| Stakeholder trust | Results → decisions, not dashboards nobody uses |
| Strong interfaces | APIs, data contracts, modular components, documented ownership |

### Core Interests

- 🤖 **AGI** — memory, reasoning stability, alignment, long-horizon planning, tool use, and constraint-aware intelligence.
- 🧠 **Agent systems** — memory architectures, retrieval policies, evaluation harnesses, controllability.
- 🔀 **AI + Data engineering convergence** — stacks where pipelines feed models and models drive products with measurable reliability.

---

## 💼 Experience

### Data Engineer — Arizona State University (ASU), Tempe, AZ
**Nov 2024 – Present**

Operating at the intersection of data reliability and mission-critical operations, focusing on pipelines and systems where correctness, security, and repeatability matter.

**Technical Focus**
- Cloud data systems on **AWS**: warehousing, secure access design, operational automation.
- Data quality and trust: validation gates, reconciliation logic, systematic error detection.
- Engineering robustness: diagnostics for distributed tasks, instrumentation, rapid triage.

**Key Contributions**
- 🏛️ **Governed pipeline architecture** — Designed warehouse and pipeline patterns with clear inputs/outputs, stable schemas, and strict permission boundaries. Prioritized secure-by-default designs: least-privilege access, traceable execution, auditable flows.
- ✅ **Data quality as a system** — Implemented validation logic and discrepancy detection to prevent silent failures. Built repeatable reconciliation checks for downstream consumer trust without manual verification loops.
- 🚦 **Operational readiness** — Developed automated diagnostics and reliability checks (Python + C++) to reduce time-to-detect and time-to-recover. Designed workflows that anticipate failure modes (partial loads, schema drift, missing partitions, delayed upstream jobs).

---

### Assistant Content & SEO Manager — NHL, Sportskeeda (India)
**Dec 2023 – Jul 2024**

A hybrid role combining analytics, performance strategy, forecasting, and operational execution with direct impact on business outcomes.

**Key Contributions**
- 📊 **KPI ownership** — Managed performance analytics across editorial, product, growth, and operations stakeholders. Translated metrics into action: not "what happened," but "what to do next."
- 📈 **Forecasting & planning** — Built forecasting models and scenario planning frameworks for quarterly planning. Set measurable guardrails: target setting, risk ranges, resource allocation logic.
- ⚙️ **Automation mindset** — Automated recurring analysis and reporting workflows to reduce manual cycles and improve consistency.

---

### AI Prompt Engineer (Freelance) — Scale AI (Remote, USA)
**Oct 2023 – Jan 2024**

High-quality prompt tasks supporting SFT and RLHF workflows, strengthening intuition for model behavior under ambiguity and failure patterns (hallucination, instruction drift).

- Produced high volumes of prompt tasks with consistent structure, clarity, and evaluability.
- Treated prompts like interfaces: inputs, constraints, expected outputs, and test cases.
- Designed tasks to surface edge cases and reasoning breakdowns, not just happy-path outputs.

---

### Machine Learning Engineer — Uniqlabs (Develup), Bangalore
**Sep 2021 – Nov 2023**

Applied ML systems combining structured + unstructured data pipelines, model training/tuning, evaluation and iteration cycles, and integration into product workflows.

**Key Contributions**
- 🔍 **Retrieval/ranking improvements (BERT)** — Tuned and evaluated retrieval/ranking behavior systematically: isolate error types, target data quality, validate metrics after each change.
- 🔄 **ETL pipelines for ML workloads** — Built scalable data pipelines for unstructured processing, reducing latency and improving throughput to keep model data fresh and production-ready.
- 🎯 **Recommendation / skill-gap systems** — Designed systems mapping user behavior → needs → recommended learning content, focused on actionable signals over vanity metrics.

---

## 🔬 Research (Thesis)

### Policy-Driven Memory Management Architecture for Autonomous Agent Systems
**Arizona State University (ASU) · Jul 2025 – Present**

> Most agentic LLM systems fail quietly in long-horizon tasks because memory grows without control, retrieval becomes noisy, context limits force poor tradeoffs, and naïve Top-K retrieval fetches "similar" but not "useful" content. The real challenge isn't "retrieve more." It's *decide what matters now, under budget, while preserving coherence across time.*

**What I'm building**

A policy-driven cognitive memory layer for LLM agents that replaces naïve retrieval with adaptive, budget-constrained retrieval — an *operating system for agent memory*:

| Component | Role |
|---|---|
| Memory ingestion | What gets stored |
| Memory decay | What fades and why |
| Memory consolidation | What becomes durable |
| Memory arbitration | What gets selected for context |
| Evaluation harnesses | Measures stability under stress |

**Core Technical Ideas**

- **Adaptive retrieval under fixed window constraints** — Policy that weighs *similarity* (semantic relevance) × *decay* (time and persistence) × *utility* (task value / expected contribution).
- **Retrieval auction concept** — Memory items compete for inclusion via a mathematically grounded scoring function with explicit budget constraints (token limits treated like compute limits).
- **Lifecycle memory engine** — Dynamic store where items decay, consolidate, get suppressed (noise), or promoted (consistent contributors).

**Evaluation philosophy** — measure token efficiency vs. task performance, identify failure modes (forgetting, repetition, drift, contradiction), stress-test under perturbations, test multi-step coherence and tool-use reliability.

**AGI relevance** — long-horizon reasoning requires memory that is controlled, auditable, and useful. Agents need policies—not heuristics—for recall. Scalable intelligence is fundamentally a resource allocation problem.

---

## 🚀 Selected Projects

### High-Performance Video Prediction & Profiling Benchmark
**Arizona State University (ASU) · Jun 2024 – Present**

- Implemented a transformer-based forecasting approach inspired by iVideoGPT for 20+ frame prediction.
- Developed a modular evaluation and profiling framework measuring temporal coherence, error accumulation over rollouts, and system performance constraints.
- **Robustness testing** — Evaluated model stability through causal-style interventions (shift, removal, duplication) to test whether learned representations are stable or brittle.

> Real systems must tolerate distribution shifts, missing inputs, and inconsistent streams — not just work on a dataset.

---

## 📄 Publication

### Multimodal AI-Based Workload Relocation Strategy for Reducing Carbon Emissions in Multi-Cloud Environments

**IEEE Xplore · 2025** — 2nd ICECONF (International Conference on AI and Knowledge Discovery in Concurrent Engineering)

**Problem** — Multi-cloud workloads are scheduled for cost/performance, rarely for sustainability.

**Contribution** — A multimodal framework combining:
- RL (Ray RLlib)
- Deep Learning (PyTorch)
- Transformers (Hugging Face)

…to relocate workloads intelligently across clouds, reducing carbon emissions while maintaining efficiency.

**Outcome** — Demonstrated reduced carbon emissions and improved energy efficiency through policy-driven relocation decisions.

---

## 🛠️ Technical Skills

### Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)

### Data Engineering
![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)

Data warehousing · Dimensional modeling · Schema design · ETL/ELT · Data quality frameworks (Great Expectations) · Observability · Reconciliation logic · API-driven pipelines · Batch + streaming patterns

### Cloud & DevOps
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)

AWS: Redshift · Lambda · IAM · GCP: BigQuery · Composer · CI/CD · Git workflows

### AI / ML / LLM Systems
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

Transformers · LangGraph · RAG · Fine-tuning · Evaluation harnesses · RLHF · SFT · XGBoost · Keras · Vector DBs (Pinecone, LanceDB) · MLflow · Ray (RLlib)

### Analytics & Visualization
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)

Forecasting · KPI frameworks · Stakeholder reporting systems

---

## 🏆 Leadership & Professional Activities

- 📝 **Reviewer** — ICLR (International Conference on Learning Representations)
- 🤝 **Contributor** — OpenAI initiative (group-chat / context feature workstream)
- 🌐 Experienced in cross-functional leadership: product, engineering, operations, and executive-facing reporting

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

> I build for **readability**, **reproducibility**, and **ownership**.
> I treat quality as a product feature, not an afterthought.
> I respect constraints — latency, budget, tokens, and people's attention.
> I write documentation like someone will inherit my system tomorrow.

---

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=Lingavasan&color=58A6FF&style=flat-square&label=Profile+Views)

</div>
