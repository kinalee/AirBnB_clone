#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['52.91.42.130']
env.password = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDJM7rzDI/+Dy5JFc4sPUGpYPDfVM9Fqw5CP+u7Z8owDaA/vq5EFevhSRkOnF6lZ5M+oRM0Vk/NDRunnl3b5TmV6vBq8RkfladkoTuaEeY58NEGoqedXK82ed1Atuht9bQ0gvLBCmRm6LDs/VDe6bmTm/Q2FytH9qdjnxzvoSjuZQgRwU4wAXFkibyiy7JB7XQSmhoGWl6sh8+45KtDfKIGyVcAwGSknSkad78/CrIhC7cy8g+vIIHtQX12FezhkUJYSyDvRb1/9al+ILCMT4HXekTniaWfsNU885fti/sPT7p789y0GrKhMc3qfwNJohhCNzhPvtkF+YRA/vUjha9T vagrant@vagrant-ubuntu-trusty-64"

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
