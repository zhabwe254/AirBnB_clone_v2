#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of web_static"""

from fabric.api import local
from datetime import datetime
import os

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
