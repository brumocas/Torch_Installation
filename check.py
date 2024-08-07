import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("cuDNN version:", torch.backends.cudnn.version())
    print("CUDA version:", torch.version.cuda)
else:
    print("CUDA and cuDNN are not available on this system.")
