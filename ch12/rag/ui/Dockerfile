FROM python:3.14-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ui.py .
RUN useradd --create-home appuser
USER appuser

EXPOSE 8501
CMD ["streamlit", "run", "ui.py", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]
