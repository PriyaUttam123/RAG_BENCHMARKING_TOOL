from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


def retrieve_chunks(
    vector_store: FAISS,
    question: str,
    k: int = 4,
) -> List[Document]:
    """Retrieve top-k relevant document chunks for a question."""
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(question)
