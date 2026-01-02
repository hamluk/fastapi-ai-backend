from langchain_core.vectorstores import VectorStore

from app.models.upload import DocumentChunks
from app.settings import Settings


class InsightRetriever:
    def __init__(self, vector_store: VectorStore, settings: Settings):
        self.vector_store = vector_store
        self.settings = settings

    def retrieve_chunks(self, query: str) -> DocumentChunks:
        search_results = self.vector_store.similarity_search_with_score(
            query=query,
            k=self.settings.qdrant_vector_store.k,
        )

        filtered_docs = [
            doc for doc, score in search_results
            if score >= self.settings.qdrant_vector_store.similarity_threshold
        ]

        return DocumentChunks(chunks=filtered_docs)
    