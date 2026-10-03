from typing import Any, Dict, List, Optional
from langchain_community.vectorstores import FAISS

from app.rag.loader import load_pdf
from app.rag.chunker import split_documents
from app.rag.embeddings import get_embeddings
from app.rag.vector_store import build_vector_store
from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer


class PlainRAGPipeline:
    def __init__(self, pdf_path: str = "data/sample.pdf", k: int = 4):
        self.pdf_path = pdf_path
        self.k = k
        self.vector_store: Optional[FAISS] = None
        self._initialize()

    def _initialize(self):
        docs = load_pdf(self.pdf_path)
        chunks = split_documents(docs)
        embeddings = get_embeddings()
        self.vector_store = build_vector_store(chunks, embeddings=embeddings)

    def answer_question(self, question: str) -> Dict[str, Any]:
        if self.vector_store is None:
            raise RuntimeError("Vector store has not been initialized.")

        retrieved_chunks = retrieve_chunks(self.vector_store, question, k=self.k)
        contexts = [chunk.page_content for chunk in retrieved_chunks]
        answer = generate_answer(question, retrieved_chunks)

        return {
            "answer": answer,
            "contexts": contexts,
        }


_pipeline_instance: Optional[PlainRAGPipeline] = None


def get_pipeline(pdf_path: str = "data/sample.pdf", k: int = 4) -> PlainRAGPipeline:
    global _pipeline_instance
    if _pipeline_instance is None:
        _pipeline_instance = PlainRAGPipeline(pdf_path=pdf_path, k=k)
    return _pipeline_instance


def answer_question(question: str, pdf_path: str = "data/sample.pdf", k: int = 4) -> Dict[str, Any]:
    pipeline = get_pipeline(pdf_path=pdf_path, k=k)
    return pipeline.answer_question(question)
