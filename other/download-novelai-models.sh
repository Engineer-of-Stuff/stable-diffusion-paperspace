#!/bin/bash
# Download only the NovelAI image generation models and hypernetworks
aria2c -d . --bt-metadata-only=true --bt-save-metadata=true --summary-interval=0 --file-allocation=none "magnet:?xt=urn:btih:5bde442da86265b670a3e5ea3163afad2c6f8ecc&dn=novelaileak&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2F9.rarbg.com%3A2810%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce"
aria2c --select-file=65,67,71,73,76,81,82,83,84,85,86,87,88,89,90,91,92,93 "5bde442da86265b670a3e5ea3163afad2c6f8ecc.torrent"
rm novelaileak/stableckpt/extra-sd-prune/sd-prune/anime700k-64bs-0.1ucg-penultimate-1epoch-clip-ema-continue-76000.pt # aria2 downloads this file even though I told it not to
