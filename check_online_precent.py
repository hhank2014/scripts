#!/usr/bin/env python
#conding=utf-8
#by huangjie

from __future__ import division
import json
import urllib2
import MySQLdb
import commands
import sys


def Connect():

        mysql_user = "zabbix"
        mysql_passwd = "zabbix"
        mysql_db = "zabbix"
        mysql_host = "172.31.24.10"

        mysql_conn = MySQLdb.connect(host=mysql_host, user=mysql_user,passwd=mysql_passwd, db=mysql_db)
        return mysql_conn

def GetIP():

        stat, proStr = commands.getstatusoutput("ifconfig eth0 | grep netmask | awk -F 'netmask' '{print $1}'|awk '{print $2}'")
        ip =  proStr
        return ip

def GetHostId(ip):

        db = Connect()
        db_cursor = db.cursor()
        sql = "select hostid from interface where ip = \"%s\"" %(ip)
        db_cursor.execute(sql)
        result = db_cursor.fetchall()

        for i in result:
                return i[0]

def GetItemID(hostid, key):

        db = Connect()
        db_cursor = db.cursor()
        sql = "select itemid from items where hostid=\"%s\" and key_=\"%s\"" %(hostid, key)
        db_cursor.execute(sql)
        result = db_cursor.fetchall()

        for i in result:
                 return i[0]

def GetNewValue(itemid):

        db = Connect()
        db_cursor = db.cursor()
        sql = "select value from history_uint where itemid = %s order by clock desc limit 1" %(itemid)
        db_cursor.execute(sql)
        result = db_cursor.fetchall()

        for i in result:
                 return i[0] 

def GetOldValue(itemid):

        db = Connect()
        db_cursor = db.cursor()
        sql = "select value from history_uint where itemid = %s order by clock desc limit 1,1" %(itemid)
        db_cursor.execute(sql)
        result = db_cursor.fetchall()

        for i in result:
                 return i[0] 

def Result(new,old):

        if new > old:
                return '0'
        else:
                return round(abs((new - old)) / old, 4) * 100

if __name__ == "__main__":

	key = "check_online_order[%s]" %(sys.argv[1])
        ip = GetIP()
	hostid = GetHostId(ip)
	itemid = GetItemID(hostid, key)
	new = GetNewValue(itemid)
	old = GetOldValue(itemid)
	print Result(new, old)
