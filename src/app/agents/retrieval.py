from langchain_core.vectorstores import VectorStore

from app.models.upload import DocumentChunks
from app.settings import Settings


class InsightRetriever:
    """
       Retriever responsible for fetching and filtering relevant document chunks
       from a vector store.
       """
    def __init__(self, vector_store: VectorStore, settings: Settings):
        """
        Initialize the retriever with a vector store and retrieval settings.

        :param vector_store: Vector database used for similarity search
        :param settings: Application settings containing retrieval parameters
        """
        self.vector_store = vector_store
        self.settings = settings

    def retrieve_chunks(self, query: str) -> DocumentChunks:
        """
        Retrieve document chunks relevant to the given query.

        The retriever performs a similarity search and filters results
        based on a configured similarity threshold to avoid low-relevance
        context being passed to the agent.

        :param query: Search query used for similarity retrieval
        :return: DocumentChunks containing only relevant documents
        """
        search_results = self.vector_store.similarity_search_with_score(
            query=query,
            k=self.settings.qdrant_vector_store.k,
        )

        filtered_docs = [
            doc for doc, score in search_results
            if score >= self.settings.qdrant_vector_store.similarity_threshold
        ]

        return DocumentChunks(chunks=filtered_docs)
    