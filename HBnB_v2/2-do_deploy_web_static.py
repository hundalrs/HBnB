#!/usr/bin/python3
""" Fabric Script that generates a .tgz archive from the contents of the
    web_static folder in the AirBnB_clone repo
"""
from fabric.api import *
import time
import os

env.hosts = ['54.91.100.225', '34.228.13.159']


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


def do_deploy(archive_path):
    """ Deploys the tar archive to the server and unpacks it
    """
    dir_name = archive_path.split("/")[1]
    if not os.path.exists(archive_path):
        return False

    upload_file = put(archive_path, "/tmp/")
    if upload_file.failed:
        return False

    create_dir = run("mkdir -p /data/web_static/releases/{}".
                     format(dir_name[:-4]))
    if create_dir.failed:
        return Falce

    unpack = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
                 format(dir_name, dir_name[:-4]))
    if unpack.failed:
        return False

    rm_dir = run("rm /tmp/{}".format(dir_name))
    if rm_dir.failed:
        return False

    move_file = run("mv /data/web_static/releases/{}/web_static/* \
                    /data/web_static/releases/{}/".
                    format(dir_name[:-4], dir_name[:-4]))
    if move_file.failed:
        return False

    rm_not_needed = run("rm -rf /data/web_static/releases/{}/web_static/".
                        format(dir_name[:-4]))
    if rm_not_needed.failed:
        return False

    rm_sym = run("rm /data/web_static/current")
    if rm_sym.failed:
        return False

    make_sym = run("ln -sf /data/web_static/releases/{} \
                   /data/web_static/current".format(dir_name[:-4]))
    if make_sym.failed:
        return False

    return True
