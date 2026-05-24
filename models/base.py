from abc import ABC, abstractmethod
from typing import List, Dict

class BaseAssistant(ABC):
    def __init__(self):
        """Initializes the assistant wrapper and its internal state."""
        pass

    @abstractmethod
    def generate_response(self, prompt: str, history: List[Dict[str, str]]) -> str:
        """
        Generates a model response given the incoming prompt and past history.
        
        :param prompt: The current user message string.
        :param history: A list of dicts representing previous turns, e.g.:
                        [{"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello!"}]
        :return: The string response from the model.
        """
        pass