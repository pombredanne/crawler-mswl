#!/usr/bin/env python
# encoding=utf-8
'''
Created on 27/09/2012

@author: ricardo
'''

import argparse
from controllers.http_links_collector import HttpLinksCollector
        
# ArgParse definition rules
parser = argparse.ArgumentParser(description="Let's crawl a web")

parser.add_argument('url', nargs=1, help='target URL')
parser.add_argument('-n', '--number-of-levels', type=int, default=1, help='how depth the crawl will go.')

args = parser.parse_args()

target_url = args.url.pop()
depth = args.number_of_levels

# Starting level to retrieve links
level = 1;
links = {}
httpLinksCollector = HttpLinksCollector(target_url)

linksList = httpLinksCollector.retrieveLinks(target_url, depth, level)

links[target_url] = linksList

print links

