#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from web_static folder"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a .tgz archive from web_static folder"""
    dt = datetime.now()
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_name))
    if result.failed:
        return None
    return archive_name
