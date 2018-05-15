#!/usr/bin/env bash
# Bash script that sets up servers for deployment
# Update the server
sudo apt-get update

# Install NGINX if not installed
sudo apt-get install -y nginx

# Start NGINX
sudo service nginx start

# Create directories needed
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Create a fake HTML file
echo -e "<html>\n    <head>\n    </head>\n    <body>\n        Holberton School\n    </body>\n</html>" > /data/web_static/releases/test/index.html

# Give ownership of the /data/ folder to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Create a location block to serve the "current" content when /hbnb_static is typed in
sed -i "43i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}\n" /etc/nginx/sites-enabled/default

# Restart NGINX
sudo service nginx restart
