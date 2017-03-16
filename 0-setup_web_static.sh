#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir - p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
sudo echo "<html><head></head><body>Hello World</body></html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "39a\ \n\tlocation /hbtn_static {\n\t alias /data/web_static/current/hbnb_static;\n\t}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
