#!/usr/bin/env python
#conding=utf-8
#by huangjie

import commands
import zc.zk
import sys

projectname = "/" + sys.argv[1]
stat, proStr = commands.getstatusoutput('cat cafago.zk |egrep -v "^$|^sent|^send|^total"')

zk = zc.zk.ZooKeeper("192.168.221.57:2181,192.168.221.57:2182,192.168.221.57:2183")

if zk.exists(projectname):
        zk.set(projectname,proStr)
else:
        zk.create(projectname)
        zk.set(projectname,proStr)
