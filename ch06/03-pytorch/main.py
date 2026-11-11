import torch

# Use the GPU if the container can see one, otherwise the CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"PyTorch {torch.__version__}, running on: {device}")

# A small matrix multiplication on that device
x = torch.rand(1000, 1000, device=device)
print("Result shape:", (x @ x).shape)
