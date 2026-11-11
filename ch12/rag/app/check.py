"""Checks retrieval: does the right section come back for questions with a known answer?"""
from rag import COLLECTION, embed_question, qdrant

# Questions worded differently from the documents, and the section that answers each one
EXPECTED = {
    "How many GPUs am I allowed to take at once?": "Limits",
    "Where do I reserve a GPU?": "Booking GPUs",
    "Which queue is for a one-hour job?": "Queues",
    "Who has to sign off on a new model?": "Before a Release",
    "How much traffic does a new model get at first?": "Canary Releases",
    "Do I need permission to undo a bad model release?": "Rollbacks",
    "When must phone numbers be deleted from a dataset?": "Personal Data",
    "How long are trained models stored?": "Model Artifacts",
    "When does the on-call week start?": "The Rotation",
    "How quickly must I answer a page?": "Responding to Alerts",
    "Who approves an expensive new server?": "Approvals",
    "Can I buy a conference ticket with team money?": "Learning",
}

TOP_K = 3
first = in_top_k = 0
for question, section in EXPECTED.items():
    hits = qdrant.query_points(COLLECTION, query=embed_question(question), limit=TOP_K).points
    found = [h.payload["section"] for h in hits]
    first += found[0] == section
    in_top_k += section in found
    if found[0] != section:
        print(f"MISS  {question!r}: expected {section!r}, got {found}")

print(f"Right section first: {first}/{len(EXPECTED)}, in the top {TOP_K}: {in_top_k}/{len(EXPECTED)}")
