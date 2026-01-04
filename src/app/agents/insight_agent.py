from langchain_core.language_models import BaseChatModel

from app.agents.prompt import build_insight_prompt
from app.agents.retrieval import InsightRetriever
from app.models.insight import Insight, Metadata
from app.models.prompt import AIAgentPrompt
from app.models.query import InsightQuery


class InsightAgent:
    """
    Backend-facing AI agent responsible for extracting structured insights
    from retrieved knowledge chunks.

    The InsightAgent orchestrates the interaction between:
    - a language model (LLM),
    - a retriever responsible for fetching relevant context,
    - and a predefined agent prompt configuration.
    """
    def __init__(self, llm: BaseChatModel, retriever: InsightRetriever, prompt_messages: AIAgentPrompt):
        """
        Initialize the InsightAgent with all required dependencies.

        :param llm: Chat-based language model used for insight generation
        :param retriever: Retriever responsible for fetching relevant document chunks
        :param prompt_messages: Static system and instruction prompts used by the agent
        """
        self.llm = llm
        self.retriever = retriever
        self.prompt_messages = prompt_messages

    def run(self, request: InsightQuery) -> Insight:
        """
        Execute the insight extraction workflow for a given query.

        The workflow consists of:
        1. Retrieving relevant document chunks using the retriever
        2. Building a prompt that combines system instructions, context, and the user question
        3. Invoking the LLM with a structured output schema
        4. Enriching the result with metadata from the retrieved chunks

        :param request: User query containing the question and optional context
        :return: Structured Insight object validated via Pydantic
        """
        doc_chunks = self.retriever.retrieve_chunks(request.question)

        prompt = build_insight_prompt(
            question=request.question,
            prompt_message=self.prompt_messages,
            context_chunks=doc_chunks
        )

        structured_llm = self.llm.with_structured_output(Insight)

        response = structured_llm.invoke(prompt)

        response.metadata = [
            Metadata(
                chunk_id=chunk.metadata.get("chunk_id"),
                title=chunk.metadata.get("title")
            )
            for chunk in doc_chunks.chunks
        ]

        return response
