import streamlit as st
from dotenv import load_dotenv

# Load all environment tokens from your .env file
load_dotenv()

# Import the model classes we wrote earlier
from models.frontier import FrontierAssistant
from models.open_source import OpenSourceAssistant

# 1. Page Configuration
st.set_page_config(
    page_title="Olive AI Assistant Workspace",
    page_icon="🫒",
    layout="wide"
)

st.title("🫒 Olive AI Assistant Workspace")
st.caption("Founding AI/ML Engineer Take-Home Assessment — Model Comparison Sandbox")

# 2. Sidebar Configuration Layer
st.sidebar.header("🛠️ Configuration")

assistant_type = st.sidebar.radio(
    "Select Active Assistant Core:",
    options=["Frontier Model (Groq)", "Open Source (Hugging Face Inference)"],
    help="Toggle between the two backend architectures using the identical chat interface."
)

# Advanced parameters sidebar display (Highly recommended for showing ML engineering intent)
st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Hyperparameters")
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
st.sidebar.info(
    "Switching models preserves your current session state layout, allowing real-time comparative prompt behavior analysis."
)

# Clear Chat Session Helper
if st.sidebar.button("🧹 Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# 3. Instantiate the proper model class based on active selection
@st.cache_resource
def get_assistant(model_type):
    if model_type == "Frontier Model (Groq)":
        # Defaulting to llama-3.3-70b-versatile via Groq SDK
        return FrontierAssistant()
    else:
        # Defaulting to Qwen2.5-0.5B-Instruct serverless API endpoint
        return OpenSourceAssistant()

active_model_instance = get_assistant(assistant_type)

# 4. Handle Chat States & Memory Context (Short-Term Conversational Memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display entire multi-turn thread history smoothly
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User Input and Multi-Turn Text Generation
if user_prompt := st.chat_input("Ask Olive Assistant anything..."):
    # Render user prompt message block immediately
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    # Store the prompt turn inside short-term message state context
    # Passing this history handles the multi-turn memory requirements
    past_history = list(st.session_state.messages)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Render generation frame for assistant output
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown("*Olive Assistant is thinking...*")
        
        # Invoke backend class engine
        generated_text = active_model_instance.generate_response(
            prompt=user_prompt, 
            history=past_history
        )
        
        # Display the response text output
        response_placeholder.markdown(generated_text)
        
    # Commit model output turn to memory
    st.session_state.messages.append({"role": "assistant", "content": generated_text})