import ctypes

# Load the CUDA runtime library that comes with the image
cudart = ctypes.CDLL("libcudart.so.13")

version = ctypes.c_int()
cudart.cudaRuntimeGetVersion(ctypes.byref(version))
print(f"CUDA runtime {version.value // 1000}.{version.value % 1000 // 10}")

# Ask how many GPUs this container can see
count = ctypes.c_int()
error = cudart.cudaGetDeviceCount(ctypes.byref(count))
if error == 0:
    print("GPUs visible:", count.value)
else:
    print("No GPU visible (CUDA error code", error, ")")
