import wget, os, sys, signal
from huggingface_hub.hf_api import HfApi

download_dir = "embeddings"
token_delimiter = ""

total = 0
failed = 0
skipped = 0
downloaded = 0

failed_list = []

def show_stats_on_quit(*args):
    print(f"\n\nFinished! Downloaded {downloaded + skipped}/{total} embeddings.")
    print(f"Failed to download {failed} embeddings: {', '.join(failed_list)}")
    sys.exit(0)

def show_stats():
    print(f"\rDownloaded: {downloaded}, skipped existing: {skipped}, failed: {failed}...{' ':10}", end="\r")

signal.signal(signal.SIGINT, show_stats_on_quit)

api = HfApi()
models = api.list_models(author="sd-concepts-library", sort="likes", direction=-1)
total = len(models)

if not os.path.exists(download_dir):
    os.mkdir(download_dir)

print(f"Downloading {total} embeddings to {os.path.abspath(download_dir)}...\n")
for model in models:
    show_stats()

    model_id = model.modelId
    model_name = model_id.split("/")[-1]
    model_file_name = f"{token_delimiter}{model_name}{token_delimiter}.bin"
    model_path = os.path.join(download_dir, model_file_name)
    model_bin_url = f"https://huggingface.co/{model_id}/resolve/main/learned_embeds.bin"

    if os.path.exists(model_path):
        skipped += 1
        continue

    try:
        wget.download(model_bin_url, out=model_path, bar=None)
        downloaded += 1
    except Exception:
        failed += 1
        failed_list.append(f"<{model_name}>")
        continue

show_stats_on_quit()
