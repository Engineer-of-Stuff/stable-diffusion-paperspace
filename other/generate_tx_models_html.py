import argparse
import datetime
import os
import shutil
import sys
from urllib import request as ulreq

import requests
from huggingface_hub import HfApi
from PIL import ImageFile


def getsizes(uri):
    # https://stackoverflow.com/a/37709319
    # get file size *and* image size (None if not known)
    file = ulreq.urlopen(uri)
    size = file.headers.get("content-length")
    if size:
        size = int(size)
    p = ImageFile.Parser()
    while True:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size, p.image.size
            break
    file.close()
    return (size, None)


parser = argparse.ArgumentParser()
parser.add_argument('out_file', nargs='?', help='file to save to')
args = parser.parse_args()

print('Will save to file:', args.out_file)

# Get list of models under the sd-concepts-library organization
print('Getting list of models...')
api = HfApi()
models_list = []
for model in api.list_models(author="sd-concepts-library"):
    models_list.append(model.modelId.replace('sd-concepts-library/', ''))
models_list.sort()

html_struct = """<!DOCTYPE html>
<html lang="en">
<head>
  <title>Stable Diffusion Texual Inversion Models</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
</head>
<body>
<style>
  .img-wrapper {
    display: flex;
    margin-top: 40px;
  }

  .img1,
  .img2,
  .img3 {}

  .thumbnail {
    height: 185px;
  }

  .model-link {}

  .model-title {
    margin-top: 100px;
  }

  .model-link-wrapper {}
</style>
<div class="container" style="margin-bottom: 180px;">
 <div class="jumbotron text-center" style="margin: 45px;"><h1>Stable Diffusion Texual Inversion Models</h1></div>
  <p><i>Page updates daily. Last updated {datetime.datetime.now().strftime("%A, %B %d %Y")}.</i></p>

<p>
  Generated from <a href="https://huggingface.co/sd-concepts-library">huggingface.co/sd-concepts-library</a>
</p>

<p>
  Downloaded models are straight from the HuggingFace repositories and are named learned_embeds.bin. Rename to model_name.pt
</p>


<br><hr>
"""

i = 1
for model_name in models_list:

    if i == 3:
        break

    print(f'{i}/{len(models_list)} -> {model_name}')
    # if os.path.exists(f'{model_name}/learned_embeds.bin'):  # double check the file exists since sometimes it hasn't been uploaded yet
    #     shutil.move(f'{model_name}/learned_embeds.bin', f'{model_name}/{model_name}.pt')
    #     pass
    # else:
    #     continue

    # Images can be in a few different formats, figure out which one it's in
    img_type = None
    img_width = None
    for type in ['jpeg', 'png', 'jpg']:
        r = requests.head(f'https://huggingface.co/sd-concepts-library/{model_name}/resolve/main/concept_images/0.{type}', allow_redirects=True)
        if r.status_code == 200:
            img_type = type
            img_width = getsizes(f'https://huggingface.co/sd-concepts-library/{model_name}/resolve/main/concept_images/0.{type}')[1][0]
            break

    html_struct = html_struct + f"""<h3 class="model-title">{model_name}</h3>
    <p><a class="model-link" href="https://huggingface.co/sd-concepts-library/{model_name}/resolve/main/learned_embeds.bin">Download {model_name}</a></p>
    <p><a class="model-link" href="https://huggingface.co/sd-concepts-library/{model_name}/">View Repository</a></p>
    <div class="img-wrapper">
      <div class="img1" style="width:{img_width}px;">
        <img class="thumbnail" src="https://huggingface.co/sd-concepts-library/{model_name}/resolve/main/concept_images/0.{img_type}">
      </div>
      <div class="img2" style="width:{img_width}px;">
        <img class="thumbnail" src="https://huggingface.co/sd-concepts-library/{model_name}/resolve/main/concept_images/1.{img_type}">
      </div>
      <div class="img3" style="width:{img_width}px;">
        <img class="thumbnail" src="https://huggingface.co/sd-concepts-library/{model_name}/resolve/main/concept_images/2.{img_type}">
      </div>
    </div>"""
    i = i + 1

html_struct = html_struct + '</div></body></html>'

f = open(args.out_file, 'w')
f.write(html_struct)
f.close()
