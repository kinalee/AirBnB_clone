#!/usr/bin/python3
"""
doc
"""
import os
from fabric.api import *

env.hosts = ['52.91.42.130', '54.209.38.142']


def do_deploy(archive_path):
    """
    doc
    """
    if not os.path.exists(archive_path):
        return False

    fn1 = archive_path.split("/")[-1]
    fn2 = fn1.split(".")[0]
    path1 = "/data/web_static/current"
    path2 = "/data/web_static/releases"

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p %s/%s/" % (path2, fn2))
        run("sudo tar -xzf /tmp/%s -C %s/%s" % (fn1, path2, fn2))
        run("sudo rm /tmp/%s" % fn1)
        run("sudo rm -fr %s" % (path1))
        run("sudo mv -f %s/%s/web_static/* %s/%s" % (path2, fn2, path2, fn2))
        run("sudo rm -rf %s/" % path1)
        run("sudo ln -s %s/%s/ %s/" % (path2, fn2, path1))
        return True
    except:
        return False
