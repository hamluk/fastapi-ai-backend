from uuid import uuid4
from pydantic import Field, field_validator, BaseModel


class Insight(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    summary: str
    confidence: float

    @field_validator("confidence")
    @classmethod
    def clamp_confidence(cls, v):
        if v is None:
            return 0.0
        if v < 0:
            return 0.0
        if v > 1:
            return 1.0
        return float(v)