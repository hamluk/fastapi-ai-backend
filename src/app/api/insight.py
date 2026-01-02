from fastapi import APIRouter, Depends
from langchain_core.language_models import BaseChatModel

from app.chains.insight_chain import run_insight_chain
from app.dependencies.llm import init_openai_chat_model
from app.models.insight import Insight
from app.models.query import InsightQuery
from app.prompts.loader import load_prompt_messages
from app.settings import get_settings, Settings

router = APIRouter()


@router.post(path="/query", response_model=Insight)
def create_insight(
        request: InsightQuery,
        settings: Settings = Depends(get_settings),
        llm: BaseChatModel = Depends(init_openai_chat_model)
):
    """
    Post Insights Endpoint: Creates a new insight to a given context and related question.

    :param request: Query object
    :param settings: Settings object
    :param llm: Language Model object
    :return:
    """

    prompt_messages = load_prompt_messages(
        settings.prompt.insight_path,
        settings.prompt.insight_version
    )

    response = run_insight_chain(
        prompt_messages,
        llm,
        request.question,
        request.context
    )

    return response
