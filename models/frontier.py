import os
from groq import Groq
from typing import List, Dict
from models.base import BaseAssistant

class FrontierAssistant(BaseAssistant):
    def __init__(self, model_name: str = "llama-3.3-70b-versatile"):
        super().__init__()
        # Initialize Groq client; it will automatically fetch GROQ_API_KEY from environment variables
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model_name = model_name

    def generate_response(self, prompt: str, history: List[Dict[str, str]]) -> str:
        # Assemble message thread for multi-turn validation
        messages = []
        for turn in history:
            messages.append({"role": turn["role"], "content": turn["content"]})
        
        messages.append({"role": "user", "content": prompt})
        
        try:
            # Query the Groq hardware accelerated endpoint
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error interacting with Groq Frontier API: {str(e)}"