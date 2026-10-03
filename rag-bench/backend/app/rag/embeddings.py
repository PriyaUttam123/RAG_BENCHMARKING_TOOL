from typing import Optional
from langchain_core.embeddings import Embeddings
from app.config import settings


def get_embeddings(model: Optional[str] = None) -> Embeddings:
    """Return embedding model based on configured API keys (Cohere or Gemini)."""
    cohere_key = (settings.cohere_api_key or "").strip()
    gemini_key = (settings.gemini_api_key or "").strip()

    if cohere_key:
        from langchain_cohere import CohereEmbeddings

        model_name = model or "embed-english-v3.0"
        return CohereEmbeddings(
            cohere_api_key=cohere_key,
            model=model_name,
        )

    if gemini_key:
        from langchain_google_genai import GoogleGenerativeAIEmbeddings

        model_name = model or "models/gemini-embedding-001"
        return GoogleGenerativeAIEmbeddings(
            model=model_name,
            google_api_key=gemini_key,
        )

    raise ValueError("Neither COHERE_API_KEY nor GEMINI_API_KEY is configured in settings.")
