#!/usr/bin/puppet
# Puppet manifest to setup web servers for deployment of web_static

# Install nginx if not installed
package { 'nginx':
  ensure => installed,
}

# Create necessary folders
file { '/data/':
  ensure => directory,
}

file { '/data/web_static/':
  ensure => directory,
}

file { '/data/web_static/releases/':
  ensure => directory,
}

file { '/data/web_static/shared/':
  ensure => directory,
}

file { '/data/web_static/releases/test/':
  ensure => directory,
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test/',
  require => File['/data/web_static/releases/test/index.html'],
}

# Give ownership to the ubuntu user and group
exec { 'chown_web_static':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => ['/bin', '/usr/bin/'],
  require => File['/data/web_static/'],
}

# Update Nginx configuration
file_line { 'nginx_config':
  path    => '/etc/nginx/sites-available/default',
  line    => "location /hbnb_static {\n\talias /data/web_static/current/;\n}",
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['nginx_config'],
}
