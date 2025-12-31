from fastapi import APIRouter

from app.models.insight import Insight
from app.models.query import InsightQuery

router = APIRouter()


@router.post(path="/query", response_model=InsightQuery)
def create_insight(
        request: InsightQuery
):
    """
    Post Insights Endpoint: Creates a new insight to a given context and related question.

    :param request: Query object
    :return:
    """

    response = Insight(
        title="Dummy Insight",
        summary="Dummy Summary",
        confidence=0.0
    )
    return {"insight": response}
