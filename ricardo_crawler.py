#!/usr/bin/env python
# encoding=utf-8
'''
Created on 27/09/2012

@author: ricardo
'''

import argparse
from controllers.http_links_collector import HttpLinksCollector

class RicardoCrawler:
    '''RicardoCrawler class to crawl a web using system parameters.
    
    '''
    
    def __init__(self):
        '''Init method
        '''
        
        pass

    def crawler_start(self):
        '''Method to start crawling.
            * Checks input parameters.
            * returns the result of crawling printing a dictionary on the screen.
        
        '''

        # ArgParse definition rules
        parser = argparse.ArgumentParser(description="Let's crawl a web")
        
        parser.add_argument('url', nargs=1, help='target URL')
        parser.add_argument('-n', '--number-of-levels', type = int, \
                            default = 1, help = 'how depth the crawl will go.')
        
        # Create argument object
        args = parser.parse_args()
        
        target_url = args.url.pop()
        depth = args.number_of_levels
        
        # Starting level to retrieve links
        level = 1
        links = {}
        http_links_collector = HttpLinksCollector(target_url)
        
        links_list = http_links_collector.\
            retrieve_links(target_url, depth, level)
        
        links[target_url] = links_list
        
        print links

if __name__ == '__main__':
    RC = RicardoCrawler()
    RC.crawler_start()
        
