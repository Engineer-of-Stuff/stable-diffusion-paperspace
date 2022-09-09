#->`--FINAL GUI RETARD GUIDE--`<-#
##->"HE WHO SHALL NOT BE NAMED"<-##
**->The definitive Stable Diffusion experience ™<-**

**->[---NEW FEATURE SHOWCASE & HOWTO---](https://github.com/AUTOMATIC1111/stable-diffusion-webui-feature-showcase)<-**
Notable: Inpainting/Outpainting, Live generation preview, Tiling, Upscaling, 4gb support
==(Basic) CPU-only guide available [**Here**](https://rentry.org/cputard)==
==[**Japanese guide here 日本語ガイド**](https://news.livedoor.com/article/detail/22794512/)==

Special thanks to all anons who contributed
!!! note Guide

**Step 1:** [**Install Git**](https://github.com/git-for-windows/git/releases/download/v2.37.3.windows.1/Git-2.37.3-64-bit.exe) [(page)](https://git-scm.com/download/win)

**Step 2:** Clone the WebUI repo to your desired location in a Git bash terminal:
`git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui`
**OR** download the WebUI repo .zip [**HERE**](https://github.com/AUTOMATIC1111/stable-diffusion-webui/archive/refs/heads/master.zip) and extract
*(git clone is easier to update since you can just type `git pull`in the directory)*

**Step 3:** Download the 1.4 AI model from [huggingface](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original) (requires signup) or [**HERE**](https://drive.yerf.org/wl/?id=EBfTrmcCCUAGaQBXVIj5lJmEhjoP1tgl) 
[(torrent magnet)](magnet:?xt=urn:btih:3a4a612d75ed088ea542acac52f9f45987488d1c&dn=sd-v1-4.ckpt&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337)
==(NEW 9/7)== Alternate 1.4 Waifu model trained on an additional **56k** Danbooru images [**HERE**](https://thisanimedoesnotexist.ai/downloads/wd-v1-2-full-ema.ckpt) 
[(mirror)](http://wd.links.sd:8880/wd-v1-2-full-ema.ckpt) [(torrent magnet)](magnet:?xt=urn:btih:INEYUMLLBBMZF22IIP4AEXLUK6XQKCSD&dn=wd-v1-2-full-ema.ckpt&xl=7703810927&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce) 
*(Note: Uncompressed, several GB larger than normal model)*
[comparison](https://cdn.discordapp.com/attachments/930499731451428926/1017258164439220254/unknown.png)

**Step 4:** Rename your .ckpt file to "model.ckpt", and place it in `stable-diffusion-webui-master`

**Step 5 (Optional):** Download and place [**GFPGANv1.3.pth**](https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth) into the master webUI directory

**Step 6:** [**Install Python 3.10.6**](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe) [(page)](https://www.python.org/downloads/windows/)

**Step 7:** Run `webui.bat` from Windows Explorer. Run it as normal user, **not** as administrator.
- Wait patiently while it installs dependencies and does a first time run. 
It may *seem* "stuck" but it isn't. It may take up to 10-15 minutes.
==And you're done!==

**==Usage:==**
- Open webui.bat
- After loading the model it should give you a LAN address such as **'127.0.0.1:7860'**
- Enter the address into your browser to enter the GUI environment

!!! info RUNNING ON 4GB
It is possible to run the Stable Diffusion webui on 4gb Vram with **some modifications:**
- Edit `webui.bat` 
- In line **5** after ` COMMANDLINE_ARGS=` , enter your desired parameters:
**Example:** `COMMANDLINE_ARGS=--medvram --opt-split-attention` 

- If you have 4GB VRAM and want to make 512x512 (or maybe up to 640x640) images, use `--medvram`.
- If you have 4GB VRAM and want to make 512x512 images, but you get an out of memory error with `--medvram`, use `--medvram --opt-split-attention` instead.
- If you have 4GB VRAM and want to make 512x512 images, and you still get an out of memory error, use `--lowvram --always-batch-cond-uncond --opt-split-attention` instead.
- If you have 4GB VRAM and want to make images larger than you can with `--medvram`, use `--lowvram --opt-split-attention`.
- If you have **more VRAM** and want to make larger images than you can usually make, use `--medvram --opt-split-attention`. 
You can use `--lowvram` also but the effect will likely be barely noticeable.
**Otherwise, do not use any of these**

- **NOTE:** 
If you get a **green screen** instead of generated pictures, you have a card that doesn't support half precision floating point numbers
 You must use `--precision full --no-half` in addition to other flags, and the model will take much more space in VRAM

!!! note LINKS/NOTES/TIPS

->==-----**LINKS**-----==<-
- Build great aesthetic prompts using the [prompt builder](https://promptomania.com/stable-diffusion-prompt-builder/)
- Check out the wiki https://wiki.installgentoo.com/wiki/Stable_Diffusion
- Japanese keywords: https://chara-zokusei.jp/question_list
- Use [Darkreader](https://darkreader.org/) to change your Gradio theme to dark mode
- [Stable diffusion WebUI repo](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Waifu Diffusion huggingface page](https://huggingface.co/hakurei/waifu-diffusion)

->==-----**TROUBLESHOOTING**-----==<-
- if your version of Python is not in PATH (or if another version is) 
create or modify webui.settings.bat in the root folder (same place as webui.bat)
add the line set PYTHON=python to say the full path to your python executable: `set PYTHON=B:\soft\Python310\python.exe`
You can do this for python, but not for git.
- The installer creates a python virtual environment, so none of installed modules will affect your system installation of python if you had one prior to installing this.
- To prevent the creation of virtual environment and use your system python, edit webui.bat replacing set `VENV_DIR=venv` with `set VENV_DIR=`
- webui.bat installs requirements from files `requirements_versions.txt`, which lists versions for modules specifically compatible with Python 3.10.6. 
If you choose to install for a different version of python, editing webui.bat to have set REQS_FILE=requirements.txt instead of set REQS_FILE=requirements_versions.txt may help (but I still reccomend you to just use the recommended version of python).
- If you feel you broke something and want to reinstall from scratch, delete directories: venv, repositories.
- If your output is a jumbled rainbow mess your image resolution is set TOO LOW
- Having too high of a CFG level will also introduce rainbow distortion, your CFG shouldn't be set above 20
- On older systems, you may have to change `cudatoolkit=11.3` to `cudatoolkit=9.0`
- Make sure your installation is on the C: drive
- This guide is designed for NVIDIA GPUs *only*, as stable diffusion requires cuda cores.
  AMD users should try https://rentry.org/sdamd

->==-----**TIPS**-----==<-
- You can drag your favorite result from the output tab on the right **back into** img2img for further iteration
- The **k_euler_a** and **k_dpm_2_a** samplers give vastly different, more intricate results from the same seed & prompt
- Unlike other samplers, **k_euler_a** can generate high quality results from low steps. Try it with 10-25 instead of 50
- The seed for each generated result is in the output filename if you want to revisit it
- Using the same keywords as a generated image in img2img produces interesting variants
- It's recommended to have your prompts be at least 512 pixels in *one* dimension, or a 384x384 square at the smallest
   Anything smaller will have heavy artifacting
- 512x512 will always yield the most accurate results as the model was trained at that resolution
- Try Low strength (0.3-0.4) + High CFG in img2img for interesting outputs
- You can use Japanese Unicode characters in prompts

->==-----**Changing UI Defaults**-----==<-
- After running once, a `ui-config.json` file appears in webui master directory:
Edit values to your liking and the next time you launch the program they will be applied.

->==-----**Running Online**-----==<-
- Use --share option to run online. You will get a xxx.app.gradio link. This is the intended way to use the program in collabs.
- Use --listen to make the server listen to network connections. This will allow computers on local newtork to access the UI, and if you configure port forwarding, also computers on the internet.
- Use --port xxxx to make the server listen on a specific port, xxxx being the wanted port. Remember that all ports below 1024 needs root/admin rights, for this reason it is advised to use a port above 1024. Defaults to port 7860 if available.

!!! info RUNNING ON WINDOWS 7/CONDA
(You can also try this method if the traditional install isn't working)
Windows 7 does **not** allow for directly installing the version of Python recommended in this guide on it's own.
However, it does allow for installing the latest versions of Python within **Conda:**
- **Follow all the same steps from the main guide, up to Step 5**
- Download Miniconda [HERE](https://docs.conda.io/en/latest/miniconda.html). Download Miniconda 3
- Install Miniconda in the default location. Install for **all users**. 
Uncheck "Register Miniconda as the system Python 3.9" unless you want to
- Open Anaconda Prompt (miniconda3)
- In Miniconda, navigate to the `/stable-diffusion-webui-master` folder wherever you downloaded using "cd" to jump folders.
(Or just type "cd" followed by a space, and then *drag the folder into* the Anaconda prompt.)
- Type the following commands to make an environment and install the necessary dependencies:
- `conda create --name qwe`
(You can name it whatever you want instead of qwe)
- `conda activate qwe`
- `conda install python`
- `conda install git`
- `webui.bat`
(Note: it may seem like it's stuck on "Installing torch" in the beginning. This is normal and should take 10-15 minutes)
==It should now be ready to use==

**RUNNING:**
- Navigate to `/stable-diffusion-webui-master` in Miniconda
- Type `conda activate qwe` 
(You will need to type 'conda activate qwe' every time you wish to run webui)
- Type `webui.bat`
- After loading the model it should give you a LAN address such as '**127.0.0.1:7860**'
Enter the address into your browser to enter the GUI environment

!!! info EXTRAS

**--OLD MODEL--**
The original v1.3 leaked model from June can be downloaded here:
https://drinkordiecdn.lol/sd-v1-3-full-ema.ckpt
Backup Download: https://download1980.mediafire.com/3nu6nlhy92ag/wnlyj8vikn2kpzn/sd-v1-3-full-ema.ckpt
Torrent Magnet: https://rentry.co/6gocs

**--OLD GUIDE--**
The original hlky guide (replaced as of 9/8/22) is here: https://rentry.org/GUItard
The original guide (replaced as of 8/25/22) is here: https://rentry.org/kretard

->**APPROXIMADE RENDER TIME BY GPU (50 steps)**<-
![Time](https://i.ibb.co/yd7SZ32/chartthin.png)
->**SAMPLER COMPARISON**<-
![Sampler Comparison](https://i.ibb.co/vm4fm7L/1661440027115223.jpg)