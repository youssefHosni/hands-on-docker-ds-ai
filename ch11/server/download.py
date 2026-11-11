import os

from huggingface_hub import snapshot_download

# Download only what the pipeline needs: the configuration, the tokenizer and the weights
path = snapshot_download(
    os.environ["MODEL_ID"],
    revision=os.environ["MODEL_REVISION"],
    allow_patterns=["config.json", "tokenizer_config.json", "vocab.txt", "model.safetensors"],
)
print("Model saved in", path)
