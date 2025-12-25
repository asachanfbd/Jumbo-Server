from typing import List, Dict
from src.app.core.interfaces import IHistoryManager

class InMemoryHistory(IHistoryManager):
    def __init__(self):
        self._history: List[Dict[str, str]] = []

    def get_history(self) -> List[Dict[str, str]]:
        return self._history.copy()

    def add_message(self, role: str, content: str):
        self._history.append({"role": role, "content": content})
