# coding=UTF-8
'''
Created on 27/09/2012

@author: ricardo
'''

from url_content_retrieve import UrlContentRetrieve

class HttpLinksCollector:

    def __init__(self, startingURL):
        '''Initialize to set urlContentRetrieve object with startingURL.
        
        Keyword arguments:
        startingURL -- URL to start crawling.

        '''
        
        self.urlContentRetrieve = UrlContentRetrieve(startingURL)
    
    def retrieveLinks(self, target_url, depth=1, level=1):
        '''
        Retrieve links from url content until defined depth organized in levels.
        
        Keyword arguments:
        target_url -- URL to analyze content and retrive links.
        depth -- Depth of links to analyze.
        level -- Level in which start to analyze.
        
        '''

        links = {}

        soup_code = self.urlContentRetrieve.urlContent(target_url)

        if depth >= level:
            for link in soup_code.findAll('a') :
                if link.has_key('href'):
                    hrefLink = link['href']
                    try:
                        sublinks = (self.retrieveLinks(hrefLink, depth, level + 1))
                        links[hrefLink] = sublinks
                    except ValueError:
                        # La Url no es correcta 
                        print "URL is not correct:\t" + link['href']
        return links
