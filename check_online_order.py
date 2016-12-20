#!/usr/bin/env python
#coding:utf8

import json
import sys

file = open("/tmp/cart_order","r")
data = file.readline()
json_data = json.loads(data)
file.close()

print json_data[sys.argv[1]],
