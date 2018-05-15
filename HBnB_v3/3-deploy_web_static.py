#!/usr/bin/python3
""" script that generates a .tgz archive from the contents of
the web_static folder of the AirBnB Clone repo and distributes
an archive to my web servers using the function do_deploy
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os


env.hosts = ['54.86.111.122', '34.228.26.238']
env.user = 'ubuntu'


def do_pack():
    """ function generates a tgz archive from the contents of
    the web_static folder of the AirBnB clone
    """
    try:
        my_time = datetime.now().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        my_file = 'versions/web_static_' + my_time + '.tgz'
        local('tar -vzcf {} web_static'.format(my_file))
        return (my_file)
    except:
        return None


def do_deploy(archive_path):
    """ function distrubtes an archive to my web servers
    """
    path_existence = os.path.exists(archive_path)
    if path_existence is False:
        return False
    try:
        path_split = archive_path.replace('/', ' ').replace('.', ' ').split()
        just_directory = path_split[0]
        no_tgz_name = path_split[1]
        full_filename = path_split[1] + '.' + path_split[2]
        folder = '/data/web_static/releases/{}/'.format(no_tgz_name)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(folder))
        run('tar -xzf /tmp/{} -C {}/'.format(full_filename, folder))
        run('rm /tmp/{}'.format(full_filename))
        run('mv {}/web_static/* {}'.format(folder, folder))
        run('rm -rf {}/web_static'.format(folder))
        current = '/data/web_static/current'
        run('rm -rf {}'.format(current))
        run('ln -s {}/ {}'.format(folder, current))
        return True
    except:
        return False


def deploy():
    """ function creates and distributes an archive to web servers
    """
    my_path = do_pack()
    if my_path is None:
        return False
    my_result = do_deploy(my_path)
    return my_result
