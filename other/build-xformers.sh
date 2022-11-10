#!/bin/bash

SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do
  DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE
done
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )

git config --system core.longpaths true
git clone https://github.com/facebookresearch/xformers.git
cd xformers
git submodule update --init --recursive
pip install -r requirements.txt

apt update
apt purge -y cuda*
apt autoremove --purge -y
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004-keyring.gpg -O /usr/share/keyrings/cuda-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/cuda-archive-keyring.gpg] https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /" | sudo tee /etc/apt/sources.list.d/cuda-ubuntu2004-x86_64.list
apt update && apt install -y cuda-command-line-tools-11-3 cuda-compat-11-3 cuda-minimal-build-11-3 cuda-compiler-11-3 cuda-libraries-dev-11-3 cuda-cupti-dev-11-3 cuda-cupti-11-3 cuda-nvcc-11-3 cuda-cudart-dev-11-3 cuda-libraries-11-3 cuda-cudart-11-3 cuda-gdb-11-3 cuda-cuobjdump-11-3 cuda-cuxxfilt-11-3 cuda-driver-dev-11-3 cuda-memcheck-11-3 cuda-nvdisasm-11-3 cuda-nvml-dev-11-3 cuda-nvprof-11-3 cuda-nvprune-11-3 cuda-nvrtc-dev-11-3 cuda-nvrtc-11-3 cuda-nvtx-11-3 cuda-sanitizer-11-3

pip uninstall -y torch torchvision torchaudio # Remove existing pytorch install.
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
pip install ninja
XFORMERS_DISABLE_FLASH_ATTN=1 NVCC_FLAGS="--use_fast_math -DXFORMERS_MEM_EFF_ATTENTION_DISABLE_BACKWARD" MAX_JOBS=8 python setup.py bdist_wheel --universal

echo -e "\n\n\nOutput whl:"
find "$DIR/xformers" -name *.whl

echo -e "Now do:\npip install --force-reinstall [path to the .whl file]"
