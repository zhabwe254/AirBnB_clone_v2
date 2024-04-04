#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static

# Install Nginx if not installed
apt-get update
apt-get -y install nginx

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create a fake HTML file for testing
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html

# Create symbolic link /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
chown -R ubuntu:ubuntu /data/
chown -R ubuntu:ubuntu /var/www/

# Update Nginx configuration
config="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "/server_name _;/a $config" /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
