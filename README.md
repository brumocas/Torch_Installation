# My PyTorch Project

## Overview

This project is designed to leverage the power of PyTorch for deep learning tasks. It includes scripts and modules that demonstrate various aspects of PyTorch functionality, from basic tensor operations to complex neural network architectures.

## Getting Started

### Prerequisites

Ensure you have the following software installed:

- [Python](https://www.python.org/downloads/)
- [PyTorch](https://pytorch.org/get-started/locally/)

### Installation

1. Clone the repository:

    ```bash
    https://github.com/brumocas/Torch_Installation.git
    cd Torch_Installation
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```
    
### PyTorch and CUDA Information

This project checks and prints the versions of PyTorch and CUDA available on your system. Run the following script to see the details:

```python
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("cuDNN version:", torch.backends.cudnn.version())
    print("CUDA version:", torch.version.cuda)
else:
    print("CUDA and cuDNN are not available on this system.")
```

### Example Scripts

- `example_script.py`: This script demonstrates basic tensor operations and neural network training using PyTorch.

### Running the Example Script

To run the example script, use:

```bash
python example_script.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PyTorch](https://pytorch.org/)
- [CUDA](https://developer.nvidia.com/cuda-zone)
- [cuDNN](https://developer.nvidia.com/cudnn)
