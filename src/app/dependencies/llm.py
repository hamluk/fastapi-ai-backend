from fastapi import Depends
from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from app.settings import get_settings, Settings


def init_openai_chat_model(settings: Settings = Depends(get_settings)) -> BaseChatModel:
    """
    Initializes and returns the LangChain OpenAI chat model

    :param settings: runtime settings for backend app
    :return: LangChain OpenAI Chat Model
    """
    return ChatOpenAI(
        model=settings.openai_model.model_name,
        temperature=settings.openai_model.temperature,
        api_key=settings.openai_model.api_key,
    )
