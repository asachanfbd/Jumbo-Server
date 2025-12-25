from fastapi.testclient import TestClient
from src.app.main import app
from src.app.core.interfaces import ILLMClient
from src.app.dependencies import get_llm_client, get_history_manager
from src.app.services.history import InMemoryHistory
from typing import List, Dict

# Mock LLM Client
class MockLLMClient(ILLMClient):
    def generate_response(self, messages: List[Dict[str, str]]) -> str:
        return "This is a mocked response."

# Reset history for tests
def get_clean_history():
    return InMemoryHistory()

client = TestClient(app)

def test_brain_api_flow():
    # Override dependencies
    app.dependency_overrides[get_llm_client] = lambda: MockLLMClient()
    # We want a fresh history for this test
    test_history = InMemoryHistory()
    app.dependency_overrides[get_history_manager] = lambda: test_history

    # 1. Send first message
    response = client.post("/jumbo-ai/brain", json={"message": "Hello"})
    assert response.status_code == 200
    assert response.text == "This is a mocked response."
    
    # Check history
    hist = test_history.get_history()
    assert len(hist) == 2
    assert hist[0]["role"] == "user"
    assert hist[0]["content"] == "Hello"
    assert hist[1]["role"] == "assistant"
    assert hist[1]["content"] == "This is a mocked response."

    # 2. Send second message
    response = client.post("/jumbo-ai/brain", json={"message": "How are you?"})
    assert response.status_code == 200
    assert response.text == "This is a mocked response."

    # Check history again
    hist = test_history.get_history()
    assert len(hist) == 4
    assert hist[2]["role"] == "user"
    assert hist[2]["content"] == "How are you?"
    assert hist[3]["role"] == "assistant"

    # Cleanup overrides
    app.dependency_overrides = {}
