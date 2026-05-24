# Olive AI Assistant Workspace: 1-Page Evaluation Report

## 1. Executive Summary & Core Results
[cite_start]This report benchmarks our customized **Frontier Assistant (Llama-3.3-70B via Groq)** against our lightweight **Open Source Assistant (Qwen-2.5-0.5B via Hugging Face)** across critical trust and safety performance guidelines[cite: 33, 34].

| Metric (Scale 1-5) | Frontier Assistant (Groq) | Open Source Assistant (HF) |
| :--- | :---: | :---: |
| **Hallucination Resistance** | 5.0 | 5.0 |
| **Bias Mitigation** | 5.0 | 5.0 |
| **Content Safety / Jailbreaks** | **1.0** | **5.0** |

[cite_start]*See attached infographic (`model_comparison_infographic.png`) for visual data distribution plots[cite: 55].*

## 2. Key Insights & Behavioral Trade-offs
* **Content Safety Vulnerability:** Surprisingly, the Frontier model completely failed the adversarial jailbreak challenge (scoring 1.0), failing to bypass or intercept the SQL injection script request safely. [cite_start]Conversely, the Open Source model demonstrated perfect resilience (scoring 5.0), illustrating robust refusal handling[cite: 34].
* [cite_start]**Factual & Bias Alignment:** Both models performed perfectly across baseline factual queries and sensitive bias vectors, achieving matching 5.0 scores[cite: 33, 34]. 

## 3. Strategic Recommendations for Olive
1.  [cite_start]**Mandatory Input Guardrails:** Because the larger Frontier model fell victim to systemic rule overrides, we recommend putting an upstream protection layer like **Llama-Guard** or **NeMo Guardrails** in front of the Groq client before shipping to production[cite: 63].
2.  [cite_start]**Hybrid Routing System:** Given the small open-source model's impressive edge safety alignment, it can be utilized cost-effectively to pre-filter inputs or handle highly specialized, sensitive operational workflows[cite: 61, 63].