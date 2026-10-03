from typing import List, Optional
from langchain_core.documents import Document
from langchain_core.language_models.chat_models import BaseChatModel
from app.config import settings


def get_llm(model: Optional[str] = None, temperature: float = 0.0) -> BaseChatModel:
    """Return LLM instance configured for Cohere or Gemini based on environment keys."""
    cohere_key = (settings.cohere_api_key or "").strip()
    gemini_key = (settings.gemini_api_key or "").strip()

    if cohere_key:
        from langchain_cohere import ChatCohere

        model_name = model or "command-r-plus-08-2024"
        return ChatCohere(
            cohere_api_key=cohere_key,
            model=model_name,
            temperature=temperature,
        )

    if gemini_key:
        from langchain_google_genai import ChatGoogleGenerativeAI

        model_name = model or "gemini-3.8-flash"
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=gemini_key,
            temperature=temperature,
        )

    raise ValueError("Neither COHERE_API_KEY nor GEMINI_API_KEY is configured in settings.")


def generate_answer(
    question: str,
    chunks: List[Document],
    llm: Optional[BaseChatModel] = None,
) -> str:
    """Generate a grounded answer to the question using ONLY the provided chunks."""
    if llm is None:
        llm = get_llm()

    context_text = "\n\n---\n\n".join(chunk.page_content for chunk in chunks)

    prompt = (
        "You are an assistant answering questions strictly based on the provided context.\n"
        "Rules:\n"
        "1. Base your answer ONLY on the directly stated facts in the context below.\n"
        "2. Do not extrapolate, speculate, or introduce any outside knowledge.\n"
        "3. If the context does not contain sufficient information to answer the question, "
        "state: 'I cannot answer this question based on the provided context.'\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question: {question}\n\n"
        "Answer:"
    )

    response = llm.invoke(prompt)
    return str(response.content).strip()
