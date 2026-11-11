import os

import requests
import streamlit as st

API_URL = os.environ.get("API_URL", "http://api:8000")

st.title("Ask the team handbook")
question = st.text_input("Your question")

if question:
    with st.spinner("Thinking..."):
        response = requests.post(f"{API_URL}/ask", json={"question": question}, timeout=120)
    response.raise_for_status()
    result = response.json()
    st.write(result["answer"])
    st.caption("Sources")
    for source in result["sources"]:
        st.caption(f"{source['file']} > {source['section']} ({source['score']})")
