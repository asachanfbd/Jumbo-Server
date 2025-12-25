from typing import List, Dict
from openai import OpenAI
from src.app.core.interfaces import ILLMClient
from src.app.core.config import settings

class OpenRouterClient(ILLMClient):
    def __init__(self):
        self.client = OpenAI(
            base_url=settings.OPENROUTER_BASE_URL,
            api_key=settings.OPENROUTER_API_KEY,
        )
        self.model = settings.LLM_MODEL

    def generate_response(self, messages: List[Dict[str, str]]) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return completion.choices[0].message.content
