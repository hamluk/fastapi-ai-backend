from fastapi import APIRouter, Depends
from langchain_core.language_models import BaseChatModel
from langchain_core.vectorstores import VectorStore

from app.chains.insight_chain import run_rag_insight_chain
from app.dependencies.llm import init_openai_chat_model
from app.dependencies.vector_store import init_qdrant_vector_store
from app.models.insight import Insight
from app.models.query import InsightQuery
from app.prompts.loader import load_prompt_messages
from app.settings import get_settings, Settings

router = APIRouter()


@router.post(path="/query", response_model=Insight)
def create_insight(
        request: InsightQuery,
        settings: Settings = Depends(get_settings),
        llm: BaseChatModel = Depends(init_openai_chat_model),
        vector_store: VectorStore = Depends(init_qdrant_vector_store)
):
    """
    Post Insights Endpoint: Creates a new insight to a given context and related question.

    :param vector_store:
    :param request: Query object
    :param settings: Settings object
    :param llm: Language Model object
    :return:
    """
    prompt_messages = load_prompt_messages(
        settings.prompt.insight_path,
        settings.prompt.insight_version
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": settings.qdrant_vector_store.k})

    response = run_rag_insight_chain(
        prompt_messages,
        llm,
        retriever,
        request.question
    )

    return response
