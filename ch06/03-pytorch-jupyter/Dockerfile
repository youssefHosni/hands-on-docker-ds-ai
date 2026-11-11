FROM pytorch/pytorch:2.15.0-cuda13.4-cudnn9-runtime
# This image's Python belongs to Ubuntu, which blocks pip unless we say so (PEP 668)
RUN pip install --no-cache-dir --break-system-packages notebook==7.6.4
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
