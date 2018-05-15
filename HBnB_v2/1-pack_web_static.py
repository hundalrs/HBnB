#!/usr/bin/python3
""" Fabric Script that generates a .tgz archive from the contents of the
    web_static folder in the AirBnB_clone repo
"""
from fabric.api import *
import time


def do_pack():
    """ Packs the contents of web_static into a tar archive
    """
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timestamp))
        return "versions/web_static_{}.tgz".format(timestamp)
    except:
        return None
