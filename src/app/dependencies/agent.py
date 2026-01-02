from fastapi import Depends
from langchain_core.language_models import BaseChatModel
from langchain_core.vectorstores import VectorStore

from app.agents.insight_agent import InsightAgent
from app.agents.retrieval import InsightRetriever
from app.dependencies.llm import init_openai_chat_model
from app.dependencies.vector_store import init_qdrant_vector_store
from app.prompts.loader import load_prompt_messages
from app.settings import get_settings, Settings


def get_insight_agent(
        llm: BaseChatModel = Depends(init_openai_chat_model),
        vector_store: VectorStore = Depends(init_qdrant_vector_store),
        settings: Settings = Depends(get_settings)
):
    retriever = InsightRetriever(vector_store, settings)
    prompt_messages = load_prompt_messages(settings.prompt.insight_path, settings.prompt.insight_version)
    return InsightAgent(llm, retriever, prompt_messages)
