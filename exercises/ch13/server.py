import csv
from pathlib import Path
from statistics import correlation, mean
from typing import Literal

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

DATA_DIR = Path("/data")

server = MCPServer("data-tools")


def read_rows(file: str) -> list[dict]:
    # .name drops any folder, so a tool call can't read outside /data
    path = DATA_DIR / Path(file).name
    if not path.exists():
        raise ToolError(f"No file {file!r}. Use list_files to see the files.")
    with open(path) as f:
        return list(csv.DictReader(f))


@server.tool()
def list_files() -> list[str]:
    """List the CSV files that can be analyzed."""
    return sorted(p.name for p in DATA_DIR.glob("*.csv"))


@server.tool()
def describe(file: str) -> dict:
    """Give the column names and the number of rows of a CSV file."""
    rows = read_rows(file)
    return {"columns": list(rows[0]), "rows": len(rows)}


@server.tool()
def column_stat(file: str, column: str, stat: Literal["mean", "min", "max"]) -> float:
    """Compute a statistic of a numeric column of a CSV file."""
    rows = read_rows(file)
    # ToolError reaches the model, and this one tells it what to do next
    if column not in rows[0]:
        raise ToolError(f"No column {column!r}. The columns are: {', '.join(rows[0])}")
    values = [float(row[column]) for row in rows]
    return round({"mean": mean, "min": min, "max": max}[stat](values), 2)


@server.tool()
def column_correlation(file: str, column_a: str, column_b: str) -> float:
    """Compute the Pearson correlation between two numeric columns of a CSV file."""
    rows = read_rows(file)
    for column in (column_a, column_b):
        if column not in rows[0]:
            raise ToolError(f"No column {column!r}. The columns are: {', '.join(rows[0])}")
    a = [float(row[column_a]) for row in rows]
    b = [float(row[column_b]) for row in rows]
    return round(correlation(a, b), 3)


# MCP over standard input and output: the client starts this container and talks to it
server.run("stdio")
