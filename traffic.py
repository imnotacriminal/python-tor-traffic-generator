#!/usr/bin/python

"""
Before you run this project, you need 2 have TOR installed and the modules. 

Ubuntu: apt-get install tor / Debian: yum install tor 

I'm Not responsible for illegal activities 

          mr criminal 2k17
"""

import socket
import socks
import urllib2
import os 
import time
import sys

if not os.geteuid() == 0:
    sys.exit('[!] Script must be run as root [!]')

os.system("service tor start")

print "Format like (http://example.com?id=whatever && http://example.com)"
URL = raw_input("What url u wanna spam with traffic: ")

try:
	while 1:
		# IP SERVER
		ipcheck_url = 'http://checkip.amazonaws.com/'
		yourip = urllib2.urlopen(ipcheck_url).read()
		print "IP OF SERVER WAS: " + yourip


		# TOR IP.
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
		socket.socket = socks.socksocket
		socksip = urllib2.urlopen(ipcheck_url).read()
		print "IP OF THE SOCKS NOW: " + socksip
		req=urllib2.Request(url=URL,headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113'})
		urllib2.urlopen(req)
		os.system("service tor restart") # new ip addr request
		time.sleep(1)

except socks.ProxyConnectionError:
	print "[X] Can't make any connection on port 9050 [X]"
	print "Are you sure TOR is running in deamon?"
	print "service tor start\n"

except KeyboardInterrupt: 
	print "[X] Program stopped [X]"

except urllib2.HTTPError: 
	print "[X] Are you sure this is the correct url? [X]"
