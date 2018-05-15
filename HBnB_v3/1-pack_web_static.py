#!/usr/bin/python3
""" script that generates a .tgz archive from the contents of
the web_static folder of the AirBnB Clone repo,
using the function do_pack
"""
from fabric.api import local
from datetime import datetime


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
