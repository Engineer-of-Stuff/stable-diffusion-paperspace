# Download all textual inversion models sd-concepts-library
# https://huggingface.co/sd-concepts-library
# Make sure to add your username and password below.

hf_username ''
hf_password = ''

# Install/Setup:
# pip install huggingface-hub
# apt update && apt install -y git-lfs
# mkdir -p /sd-concepts-library/repositories

from huggingface_hub import HfApi
import os

api = HfApi()
models_list = api.list_models(author="sd-concepts-library", sort="likes", direction=-1)
print('Downloading', len(models_list), 'models...')

i = 1
for model_info in models_list:
    print(f'\nCloning {model_info.modelId} | {i}/{len(models_list)}')
    model_name = model_info.modelId.replace('sd-concepts-library/', '')
    os.system(f'git clone --depth=1 https://{hf_username}:{hf_password}@huggingface.co/{model_info.modelId} repositories/{model_name}')
    os.system(f'rm -rf repositories/{model_name}/.git*')
    os.system(f'mv repositories/{model_name}/learned_embeds.bin {model_name}.pt')
    i = i + 1
