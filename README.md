# stable-diffusion-paperspace

_Jupyter notebooks for Paperspace._

### Getting Started

**Quickstart**
```bash
wget https://raw.githubusercontent.com/Engineer-of-Stuff/stable-diffusion-paperspace/master/StableDiffusionUI_Voldemort_paperspace.ipynb
```

Or, download the notebook file: [StableDiffusionUI_Voldemort_paperspace.ipynb](https://raw.githubusercontent.com/Engineer-of-Stuff/stable-diffusion-paperspace/master/StableDiffusionUI_Voldemort_paperspace.ipynb)

This notebook is designed to automate pretty much the entire process of getting your WebUI set up.

Guide: [docs/Paperspace Guide for Idiots.md](https://github.com/Engineer-of-Stuff/stable-diffusion-paperspace/blob/main/docs/Paperspace%20Guide%20for%20Idiots.md)

<br>

Did I break something with a new update? You can download an old version of this notebook here: https://github.com/Engineer-of-Stuff/stable-diffusion-paperspace/commits/master

<br>

### A note about Python 3.10

Python 3.10 is the recommended Python version for running the WebUI. If you encounter any issues, maybe running the WebUI in Python 3.10 will help? Paperspace uses Python 3.9 so you must run a custom container.

If you have already created a machine, delete it and create a new one following these instructions: https://docs.paperspace.com/gradient/notebooks/runtimes/#how-to-specify-a-custom-container

Make sure to use this container image: `cyberes/gradient-base-py3.10:latest`


### xformers

I've compiled wheels for a bunch of GPUs → https://github.com/Cyberes/xformers-compiled

### /other Directory

Other notebooks and old code.

### /docs Directory
- [docs/Paperspace Guide for Idiots.md](https://github.com/Engineer-of-Stuff/stable-diffusion-paperspace/blob/main/docs/Paperspace%20Guide%20for%20Idiots.md): how to install the notebook on Paperspace.

### Linux

See [stable-diffusion-webui-linux](https://github.com/Cyberes/stable-diffusion-webui-linux).
