#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import *


def do_pack():
    date = local($(date + "%Y%m%d%H%M%S"))
    local('mkdir -p versions')
    local('tar -cvzf "versions/web_static_"+date+".tgz" ./web_static')
