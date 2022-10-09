#!/bin/bash

# ONLY USE ON A PAPERSPACE NOTEBOOK

if [[ -z $1 ]]
then
    echo -e "You need to set your cuda arch. Go to https://developer.nvidia.com/cuda-gpus and find your GPU.\nThen run this again like this:\n./build-xformers.sh [your cuda arch here]"
    exit
fi


# Completly remove cuda from your system
# The container comes with cuda 11.2 installed which pytorch is incompatable with
# We MUST install cuda 11.3
apt purge -y cuda*
apt autoremove --purge -y
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004-keyring.gpg -O /usr/share/keyrings/cuda-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/cuda-archive-keyring.gpg] https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /" | sudo tee /etc/apt/sources.list.d/cuda-ubuntu2004-x86_64.list
apt update
apt install -y cuda-command-line-tools-11-3 cuda-compat-11-3 cuda-minimal-build-11-3 cuda-compiler-11-3 cuda-libraries-dev-11-3 cuda-cupti-dev-11-3 cuda-cupti-11-3 cuda-nvcc-11-3 cuda-cudart-dev-11-3 cuda-libraries-11-3 cuda-cudart-11-3 cuda-gdb-11-3 cuda-cuobjdump-11-3 cuda-cuxxfilt-11-3 cuda-driver-dev-11-3 cuda-memcheck-11-3 cuda-nvdisasm-11-3 cuda-nvml-dev-11-3 cuda-nvprof-11-3 cuda-nvprune-11-3 cuda-nvrtc-dev-11-3 cuda-nvrtc-11-3 cuda-nvtx-11-3 cuda-sanitizer-11-3

# Download xformers source
cd /notebooks/
git config --system core.longpaths true
git clone https://github.com/facebookresearch/xformers.git
cd /notebooks/xformers
git submodule update --init --recursive

# Build xformers
apt install python3.9-venv
python3 -m venv venv_xformers
source ./venv_xformers/bin/activate
pip uninstall -y torch  torchvision torchaudio # Remove existing pytorch install.
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113 # Install pytorch for cuda 11.3
pip install setuptools==49.6.0 # This was suggested by anon
# nvidia-smi -L | perl -lane 'while (/^GPU\s[0-9]+:\s(.*?)\s\(UUID:.*?\)$/g) {printf "%s\n", $1}' # Get your GPU version and set the right cuda arch
# https://developer.nvidia.com/cuda-gpus
export TORCH_CUDA_ARCH_LIST=$1
pip install -r requirements.txt
pip install -e .
