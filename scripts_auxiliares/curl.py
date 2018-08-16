#!/usr/bin/python

import sys
import pycurl
import urllib
import json
from StringIO import StringIO

def getQuery(conn,url):
	response=StringIO()
	conn.setopt(conn.URL,url)
	conn.setopt(conn.WRITEDATA,response)
	conn.perform()
	conn.close()
	return response

def postQuery(conn,url,data):
	conn.setopt(conn.URL,url)
	conn.setopt(conn.POST, 1)
	conn.setopt(conn.POSTFIELDS, data)
	conn.perform()
	status_code=conn.getinfo(pycurl.HTTP_CODE)
	conn.close()
	return status_code

def toJSON(objecttr,value):
	if "{" in value:
		par_json="{\""+objecttr+"\":"+value+"}"
		return par_json
	else:
		par_json="{\""+objecttr+"\":\""+value+"\"}"
		return par_json

method=sys.argv[1]
url_base="http://localhost:7557/devices/"
connection_request="/tasks?connection_request"

if method=='post':
	device=unicode(sys.argv[2])
	param=unicode(sys.argv[3])
	value=unicode(sys.argv[4])
	data_array=[]
	key_array=[]
	key_array.append(param)
	key_array.append(value)
	key_array.append('xsd:string')
	data_array.append(key_array)
	data=json.dumps({"name":"setParameterValues","parameterValues":data_array})
	url=url_base+device+connection_request
	print data
	print url
	c=pycurl.Curl()
	status_code=postQuery(c,url,data)
	if status_code==200:
		print status_code
		print 'OK'
	elif status_code==202:
		print status_code
		print 'Config failed'
	else:
		print status_code
		print 'otro error'

if method=='get':
	
	device=sys.argv[2]
	param=sys.argv[3]
	query=toJSON("_id",device)
	query_encoded=urllib.urlencode({"query":query})
	url=url_base+'?'+query_encoded+"&projection="+param
	print url
	c=pycurl.Curl()
	d=getQuery(c,url).getvalue()
	j=json.loads(d)[0]
	param_array=param.split('.')
	for each in param_array:
		j=j[each]
	print j['_value']