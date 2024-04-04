#!/usr/bin/python3
"""Fabric script to clean outdated archives"""

from fabric.api import env, local, run
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """Cleans outdated archives"""
    try:
        number = int(number)
        if number < 0:
            number = 0
    except ValueError:
        number = 0

    local_archives = sorted(os.listdir("versions"))
    web_server_archives = run("ls -tr /data/web_static/releases").split()

    if number == 0 or number == 1:
        number_to_keep = 1
    else:
        number_to_keep = number + 1

    # Delete local archives
    for archive in local_archives[:-number_to_keep]:
        local("rm -f versions/{}".format(archive))

    # Delete web server archives
    for archive in web_server_archives[:-number_to_keep]:
        run("rm -rf /data/web_static/releases/{}".format(archive))
