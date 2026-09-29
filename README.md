# RAG_BENCHMARKING_TOOL
Compare RAG pipeline configurations on answer quality (RAGAS), latency and cost, and find the best setup for your data.


The Problem

A RAG system has many tunable choices: chunk size, overlap, embedding model, vector store, top-k, retrieval method, LLM and prompt. Most teams pick them by gut feeling and never measure the trade-offs between quality, speed and cost.

The Solution

Upload your documents, define several pipeline configurations, and run them all against the same test questions. The tool scores every configuration with RAGAS metrics plus latency and token cost, then shows a side-by-side comparison and a recommended configuration.



Priya Uttam GitHub

License

MIT (add a LICENSE file to the repo).
