#->`-- Standard Diffusion Datasets --`<-#

[TOC]

## Quick & Easy Torrent Downloading

```bash
apt update
apt install -y aria2
aria2c "<magnet URL here>"
```

## Standard Model

**Torrent**

```bash
magnet:?xt=urn:btih:3A4A612D75ED088EA542ACAC52F9F45987488D1C&tr=udp://tracker.opentrackr.org:1337
```



**Web Download**

Voldy provided an alternative download if you don't want to use HuggingFace.

`https://drive.google.com/file/d/1wHFgl0ivCmIZv88hVZXkb8oy9qCuaBGA/view`


HuggingFace is much faster and reliable but you need to get access to the repo and provide your user token.

```bash
wget --header="'Authorization: Bearer {user_token}'" https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt -O sd-v1-4.ckpt
```



## Waifu Diffusion



**Torrent**

```bash
magnet:?xt=urn:btih:F45CECF4E9DE86DA83A78DD2CCCD7F27D5557A52&tr=udp://nyquist.localghost.org:6969
```



**Web Download**

Very slow

```bash
https://thisanimedoesnotexist.ai/downloads/wd-v1-2-full-ema.ckpt
```



**Half-Size Model**

Smaller filesize, minor shift of output vs ema model. If you're on free tier try this first, it's 3.5GB. 

```bash
magnet:?xt=urn:btih:153590FD7E93EE11D8DB951451056C362E3A9150&dn=wd-v1-2-full-ema-pruned.ckpt&tr=udp://tracker.opentrackr.org:1337
```

## WD v1.2 and SD v1.4 Merged
```bash
magnet:?xt=urn:btih:UFIV4BI4MGWFLZSKPFQ5VFLNYL24ADUQ&dn=wd1-2_sd1-4_merged.ckpt&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce
```


## trinart_stable_diffusion_v2

Another anime finetune.

The 60000 steps version is the original, the 115000 steps is the  60000 with additional training. Use the 60000 step version if the style nudging is too much.



**115000**

```bash
https://huggingface.co/naclbit/trinart_stable_diffusion_v2/resolve/main/trinart2_step115000.ckpt -O trinart2_step115000.ckpt
```



**60000**

```bash
https://huggingface.co/naclbit/trinart_stable_diffusion_v2/resolve/main/trinart2_step60000.ckpt -O trinart2_step60000.ckpt
```

## Danbooru potato epoch0

A lewd danbooru model that outputs ehh results cause it needs more training.

```bash
magnet:?xt=urn:btih:f6976fbe3b9f93469bb62eb0c4950643b09f1f83&dn=Lewd-diffusion-pruned.ckpt&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=http%3a%2f%2ftracker.nucozer-tracker.ml%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.moeking.me%3a6969%2fannounce&tr=http%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.dler.org%3a6969%2fannounce&tr=http%3a%2f%2ftracker1.bt.moack.co.kr%3a80%2fannounce&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2810%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2fbt.oiyo.tk%3a6969%2fannounce&tr=udp%3a%2f%2fopen.demonii.com%3a1337%2fannounce&tr=https%3a%2f%2ftracker.lilithraws.org%3a443%2fannounce&tr=http%3a%2f%2ftracker3.ctix.cn%3a8080%2fannounce&tr=udp%3a%2f%2fchouchou.top%3a8080%2fannounce&tr=https%3a%2f%2fopentracker.i2p.rocks%3a443%2fannounce&tr=https%3a%2f%2ftracker.nanoha.org%3a443%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce&tr=https%3a%2f%2ftracker1.520.jp%3a443%2fannounce
```


[Github mirror](https://github.com/Engineer-of-Stuff/stable-diffusion-paperspace/blob/main/Docs/Datasets.md)
