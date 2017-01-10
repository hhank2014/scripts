#!/usr/bin/env python
#conding=utf-8
#by huangjie
import urllib2
import json
import sys


def authenticate(url, header, username, password):

        data = json.dumps(
        {
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                "user": username,
                "password": password
                },
        "id": 0
        })

        request = urllib2.Request(url,data)
        for key in header:
           request.add_header(key,header[key])
        try:
           result = urllib2.urlopen(request)
        except URLError as e:
           print "Auth Failed, Please Check Your Name AndPassword:",e.code
        else:
           response = json.loads(result.read())
           result.close()
        return response['result']

def GetHost(auth):

        data = json.dumps(
        {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params":{
                        'output': 'extend',
                },
                "auth": auth,
                "id": 0
        })

        request = urllib2.Request(url,data)
        for key in header:
           request.add_header(key,header[key])
           result = urllib2.urlopen(request)
           response = json.loads(result.read())
           result.close()
           return response['result']

def getGraph(hostname, auth, graphtype, dynamic, columns):

	if (graphtype == 0):
	  selecttype = ['graphid']
	  select = 'selectGraphs'
	if (graphtype == 1):
	  selecttype = ['itemid', 'value_type']
	  select = 'selectItems'

	data = json.dumps(
	{
		'jsonrpc': '2.0',
		'method': 'host.get',
		'params': {
		select: selecttype,
		'output': ['hostid', 'host'],
		'searchByAny': 1,
	        'filter': {
	        	'host': hostname
	        }
	      },
	      'auth': auth,
	      'id': '2'
	 })
	request = urllib2.Request(url,data)
        for key in header:
        	request.add_header(key,header[key])
        	result = urllib2.urlopen(request)
        	response = json.loads(result.read())
		output = response
        	result.close()
	#return output['result'][0]['graphs']
	graphs = []
	if (graphtype == 0):
	  for i in output['result'][0]['graphs']:
	    graphs.append(i['graphid'])
	if (graphtype == 1):
	  for i in output['result'][0]['items']:
	    if int(i['value_type']) in (0, 3):
	      graphs.append(i['itemid'])
	#return graphs
	graph_list = []
	x = 0
	y = 0
	for graph in graphs:
	  graph_list.append({
	    "resourcetype": graphtype,
	    "resourceid": graph,
	    "width": "500",
	    "height": "100",
	    "x": str(x),
	    "y": str(y),
	    "colspan": "1",
	    "rowspan": "1",
	    "elements": "0",
	    "valign": "0",
	    "halign": "0",
	    "style": "0",
	    "url": "",
	    "dynamic": str(dynamic)
	  })
	  x += 1
	  if x == columns:
	    x = 0
	    y += 1

	if len(graph_list) == 0:
		sys.exit(1)
	else:
		return graph_list
def screenCreate(auth, screen_name, graphids, columns):

	if len(graphids) % columns == 0:
	  vsize = len(graphids) / columns
	else:
	  vsize = (len(graphids) / columns) + 1

	values = {
		"jsonrpc": "2.0",
		"method": "screen.create",
	        "params": [{
	        "name": screen_name,
	        "hsize": columns,
	        "vsize": vsize,
	        "screenitems": []
	        }],
	        "auth": auth,
	        "id": 2
	}
	
	for i in graphids:
		values['params'][0]['screenitems'].append(i)
	data = json.dumps(values)
	req = urllib2.Request(url, data, {'Content-Type': 'application/json-rpc'})
	response = urllib2.urlopen(req, data)
	host_get = response.read()
	output = json.loads(host_get)
	try:
	  message = output['result']
	except:
	  message = output['error']['data']
	print json.dumps(message)
 
def main():

	global url,header

	url = 'http://192.168.221.66/zabbix/api_jsonrpc.php'
	username = "Admin"
	password = "zabbix"
	header = {"Content-Type":"application/json"}
	columns = 3
	dynamic = 1
	screentype = 0
	auth = authenticate(url, header, username, password)

	for i in GetHost(auth):
		hostname = i['host']
		screen_name = i['host']
	  	graphids = getGraph(hostname, auth, screentype, dynamic, columns)
		screenCreate(auth, screen_name, graphids, columns)

if __name__ == '__main__':
	main()
