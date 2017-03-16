#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['52.91.42.130', '54.209.38.142' ]

def do_deploy(archive_path):

    if not os.path.exists(archive_path):
        return False

    fn1 = archive_path.split("/")[-1]
    fn2 = fn1.split(".")[0]
    path1 = "/data/web_static/current"
    path2 = "/data/web_static/releases"

    try:
        put(archive_path, '/tmp/')
        sudo('mkdir -p %s/%s/' % (path2, fn2))
        sudo('tar -xzf /tmp/%s -C %s/%s' % (fn1, path2, fn2))
        sudo('rm /tmp/%s' % fn1)
        sudo('mv %s/%s/web_static/* ../' % (path2, fn2))
        sudo('rm -rf %s/%s/web_static' % (path2, fn2))
        sudo('rm -rf %s/' % path1)
        sudo('ln -s %s/%s %s/' % (path2, fn2, path1))
    except:
        return False

    return True
