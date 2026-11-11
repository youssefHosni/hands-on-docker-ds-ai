import asyncio
import json
import os
import sys

import httpx2
from mcp import Client
from mcp.client.streamable_http import streamable_http_client
from openai import OpenAI

# Set by Compose from the models: section
MODEL = os.environ["LLM_MODEL"]
llm = OpenAI(base_url=os.environ["LLM_URL"], api_key="unused")

GATEWAY_URL = "http://gateway:8811/mcp"
TOKEN = os.environ["MCP_GATEWAY_AUTH_TOKEN"]

SYSTEM = """Use the tools for anything about files or about the current time. Never guess those.
When you have the answer, give it in one sentence."""

# An agent is a loop, and every loop needs a limit
MAX_STEPS = 6


async def run(question: str) -> None:
    http = httpx2.AsyncClient(headers={"Authorization": f"Bearer {TOKEN}"})
    async with Client(streamable_http_client(GATEWAY_URL, http_client=http)) as gateway:
        # The tools the model may use, in the format of the OpenAI API
        tools = [
            {
                "type": "function",
                "function": {"name": t.name, "description": t.description, "parameters": t.input_schema},
            }
            for t in (await gateway.list_tools()).tools
        ]
        messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": question}]

        for _ in range(MAX_STEPS):
            reply = llm.chat.completions.create(
                model=MODEL, temperature=0, messages=messages, tools=tools
            ).choices[0].message
            if not reply.tool_calls:
                print(reply.content)
                return

            # The model asked for tools: run them and give it the results
            messages.append(reply.model_dump(exclude_none=True))
            for call in reply.tool_calls:
                args = json.loads(call.function.arguments)
                print(f"[tool] {call.function.name} {args}")
                result = await gateway.call_tool(call.function.name, args)
                text = result.content[0].text
                print(f"[result] {text}")
                messages.append({"role": "tool", "tool_call_id": call.id, "content": text})

        print(f"Stopped after {MAX_STEPS} steps without an answer.")


asyncio.run(run(" ".join(sys.argv[1:])))
