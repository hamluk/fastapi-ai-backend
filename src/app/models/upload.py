from typing import List

from langchain_core.documents import Document
from pydantic import BaseModel


class DocumentChunks(BaseModel):
    chunks: List[Document]


class UploadResponse(BaseModel):
    success: bool
    message: str
