from typing import List, Optional
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from app.rag.embeddings import get_embeddings


def build_vector_store(
    chunks: List[Document],
    embeddings: Optional[Embeddings] = None,
) -> FAISS:
    """Build and return a FAISS vector store from document chunks."""
    if embeddings is None:
        embeddings = get_embeddings()

    return FAISS.from_documents(chunks, embeddings)
