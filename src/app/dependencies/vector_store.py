from fastapi import Depends
from langchain_core.vectorstores import VectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams

from app.settings import get_settings, Settings


def get_openai_embeddings(embedding_model: str, api_key) -> OpenAIEmbeddings:
    """
    Create and return an OpenAI embedding model instance.

    This function encapsulates embedding model initialization to keep
    vector store setup explicit and configurable. It allows embedding
    models to be swapped or adjusted without modifying retrieval logic.

    :param embedding_model: Name of the OpenAI embedding model to use
    :param api_key: OpenAI API key used for embedding generation
    :return: Initialized OpenAIEmbeddings instance
    """
    return OpenAIEmbeddings(model=embedding_model, api_key=api_key)


def init_qdrant_vector_store(settings: Settings = Depends(get_settings)) -> VectorStore:
    """
    Initialize and return the vector store used for retrieval.

    This dependency is responsible for:
    - creating the embedding model,
    - ensuring the Qdrant collection exists,
    - and returning a fully configured vector store abstraction.

    :param settings: Application settings containing vector store configuration
    :return: Configured VectorStore instance backed by Qdrant
    """
    embeddings = get_openai_embeddings(settings.qdrant_vector_store.embedding_model, settings.openai_model.api_key)

    client = QdrantClient(path=settings.qdrant_vector_store.path)

    if not client.collection_exists(collection_name=settings.qdrant_vector_store.collection_name):
        client.create_collection(
            collection_name=settings.qdrant_vector_store.collection_name,
            vectors_config=VectorParams(size=settings.qdrant_vector_store.vector_size, distance=settings.qdrant_vector_store.distance)
        )

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=settings.qdrant_vector_store.collection_name,
        embedding=embeddings,
    )

    return vector_store
