# Tunneling Proxy for Paperspace

Gradio's reverse proxy service sucks. The WebUI program integrates ngrok to fix this issue which works well but Paperspace locks your account for using any tunneling proxy service such as (who knows how many they  explicitly ban).



There is literally no easy solution for this and you must to host your own server that Paperspace doesn't know  about.
 What I do is run a [rathole](https://github.com/rapiz1/rathole) server on a $4 DigitalOcean VPS.


Paperspace may get wise to the rathole method but unless they block all external connections and preform deep packet inspection to detect rathole traffic there isn't much they can do.



### 1. Spin up a server

I've had good experiences with DigitalOcean. You can use my promo code for $200 credit over 60 days: https://m.do.co/c/08ef99974bdd

Select this machine:

<img src="https://raw.githubusercontent.com/Engineer-of-Stuff/stable-diffusion-paperspace/master/docs/assets/create-droplet.png" width=500>





### 2. Update the machine

```bash
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y --purge && reboot
```



### 3. Install rathole

```bash
sudo apt install unzip
LATEST_RELASE=$(curl -s https://api.github.com/repos/rapiz1/rathole/releases/latest | grep browser_download_url | cut -d '"' -f 4 | grep "rathole-x86_64-unknown-linux-gnu.zip")
TMP=$(mktemp -d)
wget "$LATEST_RELASE" -O $TMP/rathole-x86_64-unknown-linux-gnu.zip
sudo unzip $TMP/rathole-x86_64-unknown-linux-gnu.zip -d /usr/local/bin
rm -rf $TMP
```



### 4. Create the server's config file

First, run this command:

```bash
rathole --genkey
```

Then copy the `Private Key` section to the `local_private_key` value and fill in the other variables.



Put this in `/etc/rathole/server.toml`

```toml
[server]
bind_addr = "0.0.0.0:8823"

[server.transport]
type = "noise"

[server.transport.noise]
local_private_key = "<generated key>"

[server.services.gradio]
token = "<a password to use for this service>"
bind_addr = "0.0.0.0:9001"
```





### 5. Create a service for rathole

```bash
echo """[Unit]
Description=Rathole Server
After=network.target

[Service]
ExecStart=/usr/local/bin/rathole /etc/rathole/server.toml
Type=simple
Restart=always


[Install]
WantedBy=default.target
RequiredBy=network.target""" > /etc/systemd/system/rathole.service
sudo systemctl daemon-reload
sudo systemctl enable rathole
sudo systemctl start rathole
sudo systemctl status rathole
```



### 6. Create the client config

Make sure to copy the `Public Key` value to `remote_public_key` and fill in the other variables.

This goes in `/notebooks/rathole/client.toml`

```toml
[client]
remote_addr = "<server IP address>:8823" # The address of the server. The port must be the same with the port in `server.bind_addr`

[client.transport]
type = "noise"

[client.transport.noise]
remote_public_key = "<generated key>"

[client.transport.tcp]
keepalive_secs = 10
keepalive_interval = 5

[client.services.gradio]
token = "<a password to use for this service>"
local_addr = "127.0.0.1:7860"
```



### 7. Install rathole on the client

```bash
sudo apt install unzip
mkdir -p /notebooks/rathole/
LATEST_RELASE=$(curl -s https://api.github.com/repos/rapiz1/rathole/releases/latest | grep browser_download_url | cut -d '"' -f 4 | grep "rathole-x86_64-unknown-linux-gnu.zip")
TMP=$(mktemp -d)
wget "$LATEST_RELASE" -O $TMP/rathole-x86_64-unknown-linux-gnu.zip
sudo unzip $TMP/rathole-x86_64-unknown-linux-gnu.zip -d /notebooks/rathole/
rm -rf $TMP
```



### 8. Start rathole on the client

```bash
rathole -c /notebooks/rathole/client.toml
```



### 9. Start the WebUI

Start the WebUI with this extra arg:

```
--port 7860
```



If you're using my notebook then set `gradio_port = 7860` in the settings block.



### 10. Access the proxied WebUI

The WebUI is accessible on your server's port 9001.



## Using nginx

You can use nginx to set up domain names for your services and encrypt the traffic. Create a wildcard DNS record and point it to your server.

```nginx
# /etc/nginx/sites-enabled/rathole.conf

# Default routes
server
{
  listen [::]:80;
  listen 80;
  server_name ~(.*?)?\.t\.example\.com$ t.example.com;
  return 301 https://$host$request_uri;
}

server
{
  listen 443 ssl http2;
  listen [::]:443 ssl http2;
  server_name ~.*?\.t\.example\.com$ t.example.com;
  root /var/www/default/rathole;
  index rathole-error.html;
  location /
  {
    try_files $uri $uri/ =404;
  }
  include /etc/nginx/includes/rathole-error.conf;
  include /etc/nginx/includes/certbot-ssl.conf; # put your certbot SSL config in this file
}

# ==============================================================================
# rathole domains

# Gradio
server
{
  listen 443 ssl http2;
  listen [::]:443 ssl http2;
  server_name gradio.t.example.com;
  location /
  {
    proxy_pass http://127.0.0.1:9001;
    include /etc/nginx/includes/rathole-proxy.conf;
  }
  include /etc/nginx/includes/rathole-error.conf;
  include /etc/nginx/includes/certbot-ssl.conf;
}
```



```nginx
# /etc/nginx/includes/rathole-proxy.conf

#proxy_ssl_protocols TLSv1.2 TLSv1.3;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
# proxy_set_header Upgrade $http_upgrade;
# proxy_set_header Connection "upgrade";
proxy_connect_timeout 600;
proxy_send_timeout 600;
proxy_read_timeout 600;
send_timeout 600;
client_max_body_size 100M; # for cloudflare
```



```nginx
# /etc/nginx/includes/rathole-error.conf
# Show a 404 error instead of a 502 error to prevent dirbusting.

error_page 404 403 500 502 503 504 =404 /rathole-error.html;
location = /rathole-error.html
{
  root /var/www/default/rathole;
  index rathole-error.html;
  internal;
}
```



```html
<!-- /var/www/default/rathole/rathole-error.html -->

<html>

<head>
  <title>404 Not Found</title>
</head>

<body>
  <center>
    <h1>404 Not Found</h1>
  </center>
</body>

</html>
```



To get a wildcard Certbot SSL cert, use this command.

```bash
sudo certbot --manual --preferred-challenges=dns --no-redirect --installer nginx -d t.example.com -d *.t.example.com
```

Certbot will tell you to create some `txt` DNS records.
