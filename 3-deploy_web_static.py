#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers for deployment"""

from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'

def do_pack():
    """Creates a .tgz archive from web_static folder"""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except:
        return None

def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive
        put(archive_path, '/tmp/')
        
        # Create directory
        folder_name = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        
        # Uncompress archive
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(folder_name, folder_name))
        
        # Delete archive
        run('rm /tmp/{}.tgz'.format(folder_name))
        
        # Move contents out of subdirectory
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder_name, folder_name))
        
        # Remove empty directory
        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))
        
        # Delete symbolic link
        run('rm -rf /data/web_static/current')
        
        # Create new symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))
        
        return True
    except:
        return False

def deploy():
    """Creates and distributes an archive to web servers for deployment"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
