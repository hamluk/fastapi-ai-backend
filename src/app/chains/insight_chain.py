from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import VectorStoreRetriever

from app.models.insight import Insight
from app.prompts.loader import ChatModelPrompt


def run_rag_insight_chain(
        prompt_messages: ChatModelPrompt,
        llm: BaseChatModel,
        retriever: VectorStoreRetriever,
        question: str
) -> Insight:
    """
    Builds and runs the LangChain insight chain

    :param retriever:
    :param prompt_messages: Prompt system and human messages
    :param llm: LLM Base Chat Model
    :param context:
    :param question:
    :return: response from the insight chain as an Insight object
    """
    context = retriever.invoke(question)

    prompt_template = ChatPromptTemplate([
        ("system", prompt_messages.system),
        ("human", prompt_messages.human)
    ])

    parser = PydanticOutputParser(pydantic_object=Insight)

    chain = prompt_template | llm | parser

    response = chain.invoke({
        "format_instruction": parser.get_format_instructions(),
        "question": question,
        "context": context
    })

    return response
