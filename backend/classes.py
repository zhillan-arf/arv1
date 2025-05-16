from pydantic import BaseModel, Field
from typing import List, Union, Any

class OAIMsg(BaseModel):
    role: str
    content: Union[str, List[Any]] 


class OAIInput(BaseModel):
    session_id: str
    user_id: str
    messages: List[OAIMsg] = Field(default_factory=list)
