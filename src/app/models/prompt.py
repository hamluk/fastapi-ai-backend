from pydantic import BaseModel


class AIAgentPrompt(BaseModel):
    system: str
