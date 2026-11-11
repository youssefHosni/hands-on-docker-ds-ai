"""Asks the RAG API a few questions and prints its answers."""
import json
import urllib.request

QUESTIONS = [
    "Do I need permission to roll back a model?",
    "Can I start a model release on a Friday?",
    "Who has to approve a model release?",
    "Can I copy raw data with phone numbers to my laptop?",
    "Is my development machine running at night?",
    "What happens to a resource without a project label?",
    "Which queue is for a one-hour job at 10:00?",
    "Who is the CEO of the company?",
]

for question in QUESTIONS:
    request = urllib.request.Request(
        "http://localhost:8000/ask",
        data=json.dumps({"question": question}).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        answer = " ".join(json.load(response)["answer"].split())
    print(f"Q: {question}\nA: {answer}\n")
