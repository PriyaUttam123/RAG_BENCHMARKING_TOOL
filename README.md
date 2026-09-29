# RAG_BENCHMARKING_TOOL
Compare RAG pipeline configurations on answer quality (RAGAS), latency and cost, and find the best setup for your data.


The Problem

A RAG system has many tunable choices: chunk size, overlap, embedding model, vector store, top-k, retrieval method, LLM and prompt. Most teams pick them by gut feeling and never measure the trade-offs between quality, speed and cost.

The Solution

Upload your documents, define several pipeline configurations, and run them all against the same test questions. The tool scores every configuration with RAGAS metrics plus latency and token cost, then shows a side-by-side comparison and a recommended configuration.

Features
Upload documents (PDF/TXT) and create datasets
Generate or upload a reviewed test set of questions with reference answers
Define multiple pipeline configurations (chunk size, overlap, top-k, vector store, LLM)
Run benchmarks as background jobs with live progress
RAGAS metrics: faithfulness, answer relevancy, context precision, context recall
Latency (p50/p95) and estimated token cost per configuration
Comparison dashboard with charts and a per-question drill-down
Recommended configuration with adjustable quality / latency / cost weights
Experiment tracking with MLflow
Tech Stack
Layer	Technology
Frontend	React, TypeScript, Vite
Backend	FastAPI, Python
RAG engine	LangChain, FAISS, ChromaDB
LLM	Gemini API
Evaluation	RAGAS
Database	Supabase (PostgreSQL)
Experiment tracking	MLflow
Architecture
React UI  -->  FastAPI  -->  RAG engine (LangChain, FAISS / ChromaDB, Gemini)
                 |                      |
                 |                      +--> RAGAS evaluation
                 v
        Supabase (PostgreSQL)  +  MLflow

One benchmark run:

Pick a dataset and several configurations, then start a run.
For each configuration: chunk, embed, index, then answer every test question while recording latency and tokens.
RAGAS scores each answer against its retrieved contexts and reference answer.
Results are saved to the database and MLflow, and the dashboard renders the comparison.
<!-- Add an architecture diagram image here: docs/architecture.png -->
What Gets Benchmarked
Variable	Examples
Chunk size / overlap	256, 512, 1024 tokens
Vector store	FAISS vs ChromaDB
Top-k	3, 5, 8
Embedding model	Gemini embeddings, open-source models
Retrieval method	Dense, hybrid, reranked
LLM / prompt	Gemini, others
				

Project Structure
backend/
  app/
    api/        # routes: datasets, configs, runs, results
    core/       # settings, db client
    rag/        # loaders, chunkers, embeddings, stores, pipeline
    eval/       # test set generation, RAGAS runner, metrics
    jobs/       # background benchmark logic
  tests/
frontend/       # React + TypeScript app
docs/           # diagrams, screenshots, schema
Limitations
RAGAS uses an LLM as judge, which can be biased; scores should be read as relative comparisons, not absolute truth.
Synthetic test questions may be easier than real user queries, so a small hand-written golden set is recommended.
Small differences between configurations may be within noise; check the spread before declaring a winner.
Benchmark runs are limited by API rate limits and cost, so test sets are kept small (20 to 50 questions).
Roadmap
 Hybrid search and reranking as benchmark variables
 Compare multiple LLMs on the same retrieval
 Automated parameter search with a cost budget
 Run-to-run comparison and exportable reports
 Regression checks when the pipeline changes
Author

Priya Uttam GitHub

License

MIT (add a LICENSE file to the repo).
