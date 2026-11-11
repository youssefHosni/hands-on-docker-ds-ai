# Chapter 13 exercise: a new tool for the agent

**Task.** Add a tool to the MCP server that computes the correlation between two columns. Make the agent
use it, without changing a line of the agent.

**Answer.** `server.py` here is `ch13/tools/server.py` with one new tool, `column_correlation`. Copy it over
the original, then, from `ch13/`:

```bash
docker build -q -t data-tools:1.0 tools
docker compose restart gateway
docker compose logs gateway | grep "tools listed"
docker compose run --rm agent "Do bigger houses cost more? Use the correlation between size and price in houses.csv."
```

The gateway lists 6 tools instead of 5, and the agent calls the new one: 0.968 (the same as computing it
by hand from `houses.csv`). The gateway reads the list of tools when it starts, which is why it needs a
restart, and it starts a new container for each call, so it uses the new image. The agent got the tool
through the gateway's list, so it didn't change. Recorded run: `outputs/ch13-exercise.txt`.
