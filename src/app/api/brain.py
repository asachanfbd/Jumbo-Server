from fastapi import APIRouter, Depends, Query, Response
from src.app.core.interfaces import ILLMClient, IHistoryManager
from src.app.core.config import settings
from src.app.dependencies import get_llm_client, get_history_manager

router = APIRouter()

from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

from src.app.core.constants import SYSTEM_PROMPT

@router.post("/jumbo-ai/brain")
async def ask_brain(
    request: ChatRequest,
    llm: ILLMClient = Depends(get_llm_client),
    history: IHistoryManager = Depends(get_history_manager)
):
    # Retrieve current history
    conversation = history.get_history()
    
    # Construct prompt messages
    # Start with system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Add conversation history
    messages.extend(conversation)
    
    # Add current user message
    messages.append({"role": "user", "content": request.message})
    
    # Generate response
    response_text = llm.generate_response(messages)
    
    # Update history
    history.add_message("user", request.message)
    history.add_message("assistant", response_text)
    
    # Return response as plain text
    return Response(content=response_text, media_type="text/plain")
