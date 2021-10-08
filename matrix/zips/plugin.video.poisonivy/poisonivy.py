# -*- coding: utf-8 -*-
#  ___  ____  _  _ 
# / __)( ___)( \/ )
#( (_-. )__)  \  / 
# \___/(__)   (__) 
#
#All credits to previous ...

from sys import argv
try: #Py2
	from urlparse import parse_qsl
except ImportError: #Py3
	from urllib.parse import parse_qsl
from resources.lib.modules import router

if __name__ == '__main__':
	try:
		url = dict(parse_qsl(argv[2].replace('?', '')))
	except:
		url = {}
	router.router(url)