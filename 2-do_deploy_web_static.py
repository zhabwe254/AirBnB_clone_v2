#!/usr/bin/python3
"""Fabric script to deploy web_static to web servers"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', 'IP web-02']


def do_deploy(archive_path):
    """Deploy archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split('/')[-1]
        folder_name = filename.split('.')[0]
        path = "/data/web_static/releases/{}/".format(folder_name)

        # Upload archive
        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(path))

        # Uncompress archive
        run("tar -xzf /tmp/{} -C {}".format(filename, path))

        # Delete archive
        run("rm /tmp/{}".format(filename))

        # Move files out of inner folder
        run("mv {}web_static/* {}".format(path, path))

        # Remove empty folder
        run("rm -rf {}web_static".format(path))

        # Delete symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link
        run("ln -s {} /data/web_static/current".format(path))

        return True
    except:
        return False
