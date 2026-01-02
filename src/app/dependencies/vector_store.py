from fastapi import Depends
from langchain_core.vectorstores import VectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams

from app.settings import get_settings, Settings


def get_openai_embeddings(embedding_model: str, api_key) -> OpenAIEmbeddings:
    return OpenAIEmbeddings(model=embedding_model, api_key=api_key)


def init_qdrant_vector_store(settings: Settings = Depends(get_settings)) -> VectorStore:
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
