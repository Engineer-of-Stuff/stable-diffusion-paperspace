# Datasets

### Standard Model

**Torrent**

```bash
apt update
apt install -y aria2
aria2c "magnet:?xt=urn:btih:3A4A612D75ED088EA542ACAC52F9F45987488D1C&tr=udp://tracker.opentrackr.org:1337"
```



**Web Download**

Voldy provided an alternative download if you don't want to use HuggingFace.

https://drive.google.com/file/d/1wHFgl0ivCmIZv88hVZXkb8oy9qCuaBGA/view


HuggingFace is much faster and reliable but you need to get access to the repo and provide your user token.

```bash
wget --header="'Authorization: Bearer {user_token}'" https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt -O sd-v1-4.ckpt
```



### Waifu Diffusion



**Torrent**

```bash
apt update
apt install -y aria2
aria2c "magnet:?xt=urn:btih:F45CECF4E9DE86DA83A78DD2CCCD7F27D5557A52&tr=udp://nyquist.localghost.org:6969"
```



**Web Download**

Very slow

```bash
wget https://thisanimedoesnotexist.ai/downloads/wd-v1-2-full-ema.ckpt -O wd-v1-2-full-ema.ckpt
```



**Half-Size Model**

If you're on free tier try this first, it's 3.5GB.

```bash
apt update
apt install -y aria2
aria2c "magnet:?xt=urn:btih:153590FD7E93EE11D8DB951451056C362E3A9150&dn=wd-v1-2-full-ema-pruned.ckpt&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://tracker.leechers-paradise.org:6969&tr=udp://p4p.arenabg.ch:1337&tr=udp://tracker.internetwarriors.net:1337&tr=wss://tracker.openwebtorrent.com"
```



### trinart_stable_diffusion_v2

Another anime finetune.

The 60000 steps version is the original, the 115000 steps is the  60000 with additional training. Use the 60000 step version if the style nudging is too much.



**115000**

```bash
wget https://huggingface.co/naclbit/trinart_stable_diffusion_v2/resolve/main/trinart2_step115000.ckpt -O trinart2_step115000.ckpt
```



**60000**

```bash
wget https://huggingface.co/naclbit/trinart_stable_diffusion_v2/resolve/main/trinart2_step60000.ckpt -O trinart2_step60000.ckpt
```
