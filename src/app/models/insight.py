from pydantic import field_validator, BaseModel


class Insight(BaseModel):
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
