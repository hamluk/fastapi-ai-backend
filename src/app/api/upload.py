from uuid import uuid4

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from langchain_qdrant import QdrantVectorStore

from app.dependencies.vector_store import init_qdrant_vector_store
from app.models.upload import DocumentChunks, UploadResponse
from app.settings import Settings, get_settings

router = APIRouter()


@router.post("/chunks", response_model=UploadResponse)
def upload_chunks(
        documents: DocumentChunks,
        settings: Settings = Depends(get_settings),
        vector_store: QdrantVectorStore = Depends(init_qdrant_vector_store)
):
    """
    Upload document chunks into the vector store for later retrieval.

    This endpoint is responsible for ingesting pre-chunked documents and
    persisting them in the configured vector database. It does not perform
    chunking, embedding logic, or retrieval decisions itself.

    The vector store is injected via FastAPI dependency injection, ensuring
    that storage configuration and lifecycle management remain centralized
    and decoupled from the endpoint implementation.

    Expected behavior:
    - Rejects empty uploads early with a client error
    - Assigns stable UUIDs to each chunk
    - Persists chunks via the vector store abstraction
    - Fails explicitly if persistence does not succeed
    """
    if len(documents.chunks) == 0:
        raise HTTPException(status_code=400, detail="No chunks to upload found")

    uuids = [str(uuid4()) for _ in range(len(documents.chunks))]

    chunk_ids_added = vector_store.add_documents(documents=documents.chunks, ids=uuids)

    if len(chunk_ids_added) == 0:
        raise HTTPException(status_code=500, detail="Uploading chunks to vector store failed")

    return UploadResponse(success=True, message=f"{len(documents.chunks)} chunks uploaded")
