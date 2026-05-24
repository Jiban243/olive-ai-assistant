import os
from transformers import pipeline
from models.base import BaseAssistant
from typing import List, Dict

class OpenSourceAssistant(BaseAssistant):
    def __init__(self, model_name: str = "Qwen/Qwen2.5-0.5B-Instruct"):
        super().__init__()
        # This initializes the model directly inside the Hugging Face Space hardware
        self.pipe = pipeline("text-generation", model=model_name, device_map="auto")

    def generate_response(self, prompt: str, history: List[Dict[str, str]]) -> str:
        messages = [{"role": turn["role"], "content": turn["content"]} for turn in history]
        messages.append({"role": "user", "content": prompt})
        
        try:
            outputs = self.pipe(messages, max_new_tokens=512, temperature=0.7)
            return outputs[0]["generated_text"][-1]["content"].strip()
        except Exception as e:
            return f"Local Space Generation Error: {str(e)}"