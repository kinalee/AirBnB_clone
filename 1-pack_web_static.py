#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    name = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    local('tar -cvzf "versions/web_static_%s.tgz" ./web_static' % name)
