#!/usr/bin/env python
#coding:utf8

import json
import sys

file = open("/tmp/cart_order","r")
data = file.readline()
file.close()

json_data = json.loads(data)

paidcount  = json_data['paidcount']
count = json_data['count']
payprecent = paidcount / count

if sys.argv[1] == "payment":
        print round(payprecent,4) * 100
else:
        print json_data[sys.argv[1]],
