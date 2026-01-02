from langchain_core.language_models import BaseChatModel

from app.agents.prompt import build_insight_prompt
from app.agents.retrieval import InsightRetriever
from app.models.insight import Insight, Metadata
from app.models.prompt import AIAgentPrompt
from app.models.query import InsightQuery


class InsightAgent:
    def __init__(self, llm: BaseChatModel, retriever: InsightRetriever, prompt_messages: AIAgentPrompt):
        self.llm = llm
        self.retriever = retriever
        self.prompt_messages = prompt_messages

    def run(self, request: InsightQuery) -> Insight:
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
