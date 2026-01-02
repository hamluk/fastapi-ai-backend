from typing import List

from pydantic import field_validator, BaseModel


class Metadata(BaseModel):
    chunk_id: str
    title: str


class Insight(BaseModel):
    title: str
    summary: str
    confidence: float
    metadata: List[Metadata]

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
