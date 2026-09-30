from fastapi import FastAPI

app = FastAPI(title="RAG Benchmarking Tool API")


@app.get("/health")
def health():
    return {"status": "ok"}