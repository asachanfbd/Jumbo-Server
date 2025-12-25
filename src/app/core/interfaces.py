from abc import ABC, abstractmethod
from typing import List, Dict

class ILLMClient(ABC):
    @abstractmethod
    def generate_response(self, messages: List[Dict[str, str]]) -> str:
        pass

class IHistoryManager(ABC):
    @abstractmethod
    def get_history(self) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    def add_message(self, role: str, content: str):
        pass
