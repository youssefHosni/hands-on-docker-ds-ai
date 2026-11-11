import torch

print("PyTorch:", torch.__version__)
print("Built for CUDA:", torch.version.cuda)
print("NVIDIA GPU available:", torch.cuda.is_available())
print("Apple GPU (MPS) available:", torch.backends.mps.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
