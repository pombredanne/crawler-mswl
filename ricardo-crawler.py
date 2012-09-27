'''
Created on 27/09/2012

@author: ricardo
'''

import urllib2
from setuptools.package_index import user_agent
from urllib2 import _opener

user_agent = "Mozilla/5.0 (X11; U; Linux x86_64; en-Us) AppleWebKit/534.7 (KHTML, Like Gecko) Chrome /7.0.517.41 Safari/534.7"

_opener = urllib2.build_opener()
_opener.addheaders = [('User-agent',user_agent)]

raw_code = _opener.open("http://es.wikipedia.org/robots.txt").read()

print raw_code
