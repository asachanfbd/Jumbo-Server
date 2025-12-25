from functools import lru_cache
from src.app.core.interfaces import ILLMClient, IHistoryManager
from src.app.services.llm import OpenRouterClient
from src.app.services.history import InMemoryHistory

# Singleton instance for history to maintain state across requests
_history_instance = InMemoryHistory()

def get_history_manager() -> IHistoryManager:
    return _history_instance

@lru_cache()
def get_llm_client() -> ILLMClient:
    return OpenRouterClient()
