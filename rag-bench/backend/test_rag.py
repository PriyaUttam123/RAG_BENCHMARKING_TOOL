"""Test script for the complete end-to-end plain RAG pipeline."""

import json
from app.rag.pipeline import answer_question


def run_tests():
    sample_questions = [
        "What internship experience does Priya Uttam have, including company name and role?",
        "What are the key technical skills and web technologies mentioned?",
        "What hackathon achievements and competitive coding accomplishments are listed?",
    ]

    print("=" * 80)
    print("RUNNING END-TO-END RAG PIPELINE TEST ON data/sample.pdf")
    print("=" * 80)

    for i, question in enumerate(sample_questions, 1):
        print(f"\n[Test Question {i}]: {question}")
        result = answer_question(question)

        print("\n--- Answer ---")
        print(result["answer"])

        print(f"\n--- Retrieved Contexts ({len(result['contexts'])} chunks) ---")
        for j, context in enumerate(result["contexts"], 1):
            preview = context.strip().replace("\n", " ")
            print(f"[{j}] {preview[:150]}...")

        print("-" * 80)


if __name__ == "__main__":
    run_tests()
