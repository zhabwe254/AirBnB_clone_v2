#!/usr/bin/python3
"""Fabric script to delete out-of-date archives"""

from fabric.api import env, local, run
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    archives = local("ls -1t versions", capture=True).split("\n")
    to_delete = archives[number:]
    for archive in to_delete:
        local("rm versions/{}".format(archive))

    archives = run("ls -1t /data/web_static/releases").split("\n")
    to_delete = archives[number:]
    for archive in to_delete:
        run("rm -rf /data/web_static/releases/{}".format(archive))
