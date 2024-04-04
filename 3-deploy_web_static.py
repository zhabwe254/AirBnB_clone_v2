#!/usr/bin/python3
"""Fabric script to automate deployment"""

from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """Packs web_static into .tgz file"""
    now = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )
    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(filename))
    if result.failed:
        return None
    return filename


def do_deploy(archive_path):
    """Deploys web_static to servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1]
        folder = ("/data/web_static/releases/" + filename.split('.')[0])

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(filename, folder))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False


def deploy():
    """Full deployment"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
