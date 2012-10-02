#!/usr/bin/env python
# encoding=utf-8
'''
Created on 27/09/2012

@author: ricardo
'''

import argparse
from controllers.http_links_collector import HttpLinksCollector
        
# ArgParse definition rules
PARSER = argparse.ArgumentParser(description="Let's crawl a web")

PARSER.add_argument('url', nargs=1, help='target URL')
PARSER.add_argument('-n', '--number-of-levels', type = int, \
                    default = 1, help = 'how depth the crawl will go.')

ARGS = PARSER.parse_args()

TARGET_URL = ARGS.url.pop()
DEPTH = ARGS.number_of_levels

# Starting level to retrieve links
LEVEL = 1
LINKS = {}
HTTPLINKSCOLLECTOR = HttpLinksCollector(TARGET_URL)

LINKS_LIST = HTTPLINKSCOLLECTOR.retrieve_links(TARGET_URL, DEPTH, LEVEL)

LINKS[TARGET_URL] = LINKS_LIST

print LINKS

