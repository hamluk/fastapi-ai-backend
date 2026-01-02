from pydantic import BaseModel


class InsightQuery(BaseModel):
    question: str
