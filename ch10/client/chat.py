"""Ask a local LLM a question through its OpenAI-compatible API and print the answer as it arrives."""
import os
import sys

from openai import OpenAI

# Ollama on this machine by default. Change the two variables to use Docker Model Runner,
# or any other OpenAI-compatible server, without touching the code.
client = OpenAI(
    base_url=os.environ.get("LLM_BASE_URL", "http://localhost:11434/v1"),
    api_key="not-needed",  # local servers ignore the key, but the SDK wants one
)
model = os.environ.get("LLM_MODEL", "gemma3:1b")
question = " ".join(sys.argv[1:]) or "In one sentence, what is Docker Compose?"

stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": question}],
    temperature=0,
    stream=True,
)
for chunk in stream:
    if chunk.choices:
        print(chunk.choices[0].delta.content or "", end="", flush=True)
print()
