#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{:s}.tgz".format(date)
    local('mkdir -p versions')
    try:
        local('tar -cvzf %s ./web_static' "name")
        return name
    except:
        return None
