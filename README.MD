# 🫒 Olive AI Assistant Sandbox

[cite_start]A comprehensive model evaluation platform and interactive workspace built as part of the Founding AI/ML Engineer technical assessment[cite: 79]. [cite_start]This platform scaffolds and benchmarks a **Frontier Model Assistant** against a localized **Open Source Assistant** [cite: 1, 3, 10, 11] [cite_start]across multi-turn conversational memory [cite: 20, 21][cite_start], factual hallucination boundaries [cite: 33][cite_start], systemic bias [cite: 34][cite_start], and adversarial vulnerability[cite: 34].

---

## 🏗️ System Architecture & Directory Layout

[cite_start]The project enforces strict separation of concerns, decoupling the model inference adapters from the downstream Streamlit comparison UI [cite: 24, 94] [cite_start]and the deterministic evaluation pipeline.

```text
olive-ai-assistant/
│
├── models/                  # Extensible inference wrapper components
│   ├── __init__.py
│   ├── base.py              # Abstract class template enforcing chat signatures
│   ├── open_source.py       # Localized Ollama handler (Qwen 2.5)
│   └── frontier.py          # Hardware-accelerated Groq handler (Llama 3.3)
│
├── evaluation/              # Deterministic test engine & visual analytics
│   ├── __init__.py
│   ├── test_prompts.json    # Target dataset (Factual, Safety, Bias vectors)
│   ├── evaluate.py          # LLM-as-a-Judge execution engine
│   ├── results.json         # Raw structured evaluation outputs
│   └── visualize.py         # Matplotlib/Seaborn infographic compiler
│
├── app.py                   # Streamlit multi-turn comparative workspace UI
├── requirements.txt         # Fixed library dependencies
├── EVALUATION_REPORT.md     # 1-page executive summary data brief
└── README.md                # Documentation guide

⚡ Quickstart Setup Instructions
1. Environment Initialization
Ensure you have Python 3.10+ available on your machine. Instantiate and activate an isolated virtual environment:
# Clone and navigate to root directory
cd ~/Downloads/olive-ai-assistant

# Setup environment
python3 -m venv olive-env
source olive-env/bin/activate

# Install explicit requirements
pip install -r requirements.txt

2. Dependency Infrastructure
Configure your local environment tokens. Create a .env file in the root workspace:
GROQ_API_KEY=gsk_your_actual_groq_key_here

(Note: .env and olive-env/ are explicitly ignored via .gitignore to prevent credential exposure ).

3. Open Source Model Local Engine (Ollama)
To satisfy the deployment fallback conditions and claim the core engineering bonus milestones , the Open Source core runs completely on-device:  
A) Download and initialize the Ollama for Mac Client.
B) Fetch the targeted lightweight instruction-tuned model via terminal:
   ollama run qwen2.5:0.5b

4. Running the Interactive UI & Evaluation Engine

To launch the comparative chat app interface:
streamlit run app.py

To re-execute the automated LLM-as-a-Judge benchmark pipeline:
python evaluation/evaluate.py
python evaluation/visualize.py


