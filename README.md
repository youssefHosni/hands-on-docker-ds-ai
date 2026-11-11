# Hands-on Docker for Data Science & AI Projects (2nd Edition): code

*From your first container to LLMs and AI agents* · by Youssef Hosni (To Data & Beyond)

Every Dockerfile, Compose file and script printed in the book, one folder per chapter.
Every command in the book was run before it was printed; `outputs/` holds those runs, so you can
compare yours against them.

| Folder | Chapter |
|---|---|
| `ch01/` | 1. Docker for Data Science Projects: A Beginner-Friendly Introduction |
| `ch02/` | 2. 10 Docker Commands for 90% of Containerization Tasks (the Compose file) |
| `ch03/` | 3. Building your first Docker container for Machine Learning Applications (FastAPI) |
| `ch04/` | 4. Writing Dockerfiles for Python & ML Projects (`app/` is the final project; the other folders are the chapter's experiments) |
| `ch05/` | 5. Best Practices For Using Docker for Data Science Projects (`layers/`, `multi-stage/`, `volumes/`, `secrets/`) |
| `ch06/` | 6. 13 Docker Container Images for Generative AI & ML Projects (one folder per image that needs files) |
| `ch07/` | 7. Data, Notebooks & Dev Containers (`project/`: one data science project with a Dev Container; `hf-cache/`: caching model downloads) |
| `ch08/` | 8. Multi-Container Projects with Docker Compose (`tracking/`: MLflow + Postgres; `project/`: the full project with a trainer and an API; `airflow/`: how to run Airflow's official Compose file) |
| `ch09/` | 9. GPUs in Containers (`pytorch/`: one Dockerfile for the CPU and CUDA builds of PyTorch; `compose/`: a GPU in Compose; `toolkit/`: NVIDIA's install commands for the Container Toolkit) |
| `ch10/` | 10. Running LLMs Locally with Docker (`ollama/`: Ollama, a model pull and Open WebUI in Compose, plus a GPU override; `client/`: one Python script for Ollama and Docker Model Runner, and its Dockerfile) |
| `ch11/` | 11. Serving Models in Production Containers (`server/`: a FastAPI server for a Hugging Face model, with the model downloaded at start or inside the image, a health check, JSON logs, `/metrics` and Prometheus; `load/`: a load-test script; `vllm/`: vLLM in Compose, plus a GPU override) |
| `ch12/` | 12. Project: A RAG Application with Docker Compose (`rag/`: a folder of documents, Qdrant, an ingest job, a FastAPI answer endpoint and a Streamlit UI, with both models in Compose's `models:` section, a retrieval check, and an Ollama override) |
| `ch13/` | 13. Docker for AI Agents & MCP (`sandbox/`: a script to test a locked-down container; `tools/`: an MCP server over CSV files; `agent/`: an agent in about 60 lines; `compose.yaml`: the MCP Gateway, the model, our agent and Docker Agent) |
| `ch14/` | 14. CI/CD for Docker Images (the small API from Chapter 3, `ci/`: test and scan scripts, `.github/workflows/docker.yml`: build, test, scan and push; copy them to the root of your own repository) |
| `ch15/` | 15. Deploying Your Containers (`app/`: one image for every platform; `vm/`: Compose with Caddy; `space/`: the Hugging Face Space header; `k8s/`: Deployment, Service, model weights on a volume) |

`exercises/chNN/` holds the answer to each chapter's exercise.

## Run a chapter

```bash
cd ch01
docker build -t iris-classifier .
docker run --rm iris-classifier
```

## Versions

Tested between 30 Oct and 11 Nov 2026 with Docker Engine 29.5 and Python 3.14 (`python:3.14-slim`). Images and
packages are pinned, so the examples keep working when new versions come out.

## License

MIT, see `LICENSE`.
