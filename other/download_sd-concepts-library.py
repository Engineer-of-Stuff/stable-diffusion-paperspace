# Download all textual inversion models sd-concepts-library
# https://huggingface.co/sd-concepts-library
# Make sure to add your username and password below.

hf_username = ''
hf_password = ''

# Install/Setup:
# pip install huggingface-hub
# apt update && apt install -y git-lfs
# mkdir -p /sd-concepts-library/repositories

from huggingface_hub import HfApi
import os

api = HfApi()
models_list = api.list_models(author="sd-concepts-library")
print('Downloading', len(models_list), 'models...')

i = 1
for model_info in models_list:
    print(f'\nCloning {model_info.modelId} | {i}/{len(models_list)}')
    model_name = model_info.modelId.replace('sd-concepts-library/', '')
    os.system(f'git clone --depth=1 https://{hf_username}:{hf_password}@huggingface.co/{model_info.modelId} repositories/{model_name}') # clone with no git history
    os.system(f'rm -rf repositories/{model_name}/.git*') # delete all git stuff in the repository
    os.system(f'mv repositories/{model_name}/learned_embeds.bin {model_name}.pt') # move the bin file out of the repository and rename it to a .pt file
    i = i + 1

# Pro-tip: use this command to compress the files with 7zip max compression.
# 7z a -t7z -m0=lzma2 -mx=9 -mfb=64 -md=32m -ms=on sd-concepts-library_complete.7z sd-concepts-library/
