from fastapi import APIRouter, Depends

from app.agents.insight_agent import InsightAgent
from app.dependencies.agent import get_insight_agent
from app.models.insight import Insight
from app.models.query import InsightQuery

router = APIRouter()


@router.post(path="/query", response_model=Insight)
def create_insight(
        request: InsightQuery,
        agent: InsightAgent = Depends(get_insight_agent)
):
    """
    Post Insights Endpoint: Creates a new insight to a given context and related question.

    :param request: Query object
    :param agent: InsightAgent object
    :return:
    """
    response = agent.run(request)

    return response
