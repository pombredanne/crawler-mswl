# coding=UTF-8
'''
Created on 27/09/2012

@author: ricardo
'''

from url_content_retrieve import UrlContentRetrieve

class HttpLinksCollector:
    '''Class to manage links from url.
    '''

    def __init__(self, starting_url):
        '''Initialize to set urlContentRetrieve object with startingURL.
        
        Keyword arguments:
        starting_url -- URL to start crawling.

        '''
        
        self.url_content_retrieve = UrlContentRetrieve(starting_url)
    
    def retrieve_links(self, target_url, depth=1, level=1):
        '''
        Retrieve links from url content until defined depth organized in levels.
        
        Keyword arguments:
        target_url -- URL to analyze content and retrive links.
        depth -- Depth of links to analyze.
        level -- Level in which start to analyze.
        
        '''

        links = {}

        soup_code = self.url_content_retrieve.url_content(target_url)

        if depth >= level:
            for link in soup_code.findAll('a') :
                if link.has_key('href'):
                    href_link = link['href']
                    try:
                        sublinks = \
                            self.retrieve_links(href_link, depth, level + 1)
                        links[href_link] = sublinks
                    except ValueError:
                        # La Url no es correcta 
                        print "URL is not correct:\t" + link['href']
        return links
