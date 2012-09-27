'''
Created on 27/09/2012

@author: ricardo
'''

import urllib2
from setuptools.package_index import user_agent
from urllib2 import _opener
from BeautifulSoup import BeautifulSoup as Soup
import argparse

user_agent = "Mozilla/5.0 (X11; U; Linux x86_64; en-Us) AppleWebKit/534.7 (KHTML, Like Gecko) Chrome /7.0.517.41 Safari/534.7"

_opener = urllib2.build_opener()
_opener.addheaders = [('User-agent', user_agent)]

# Parameters
parser = argparse.ArgumentParser(description="Let's crawl a web")

parser.add_argument('url', nargs=1, help='target URL')
parser.add_argument('-n', '--number-of-levels', type=int, default=1, help='how depth the crawl will go.')

args = parser.parse_args()

target_url = args.url.pop()
depth = args.number_of_levels
print depth

# URL Decode
raw_code = _opener.open(target_url).read()

soup_code = Soup(raw_code)
links = []

for link in soup_code.findAll('a') :
         if link.has_key('href'):
            links.append(link['href'])
            print link['href']
