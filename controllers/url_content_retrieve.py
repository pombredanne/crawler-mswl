# coding=UTF-8
'''
Created on 27/09/2012

@author: ricardo
'''

import urllib2
from BeautifulSoup import BeautifulSoup as Soup

class UrlContentRetrieve:
    '''Controller class to manage url and retrieve content using BeautifulSoup.
    '''

    def __init__(self, top_url):
        '''Initializes UrlContentRetrieve with default user_agent.
        
        Keyword arguments:
        top_url -- URL from top web level.
        
        '''

        user_agent = "Mozilla/5.0 (X11; U; Linux x86_64; en-Us) \
            AppleWebKit/534.7 (KHTML, Like Gecko) Chrome \
            /7.0.517.41 Safari/534.7"

        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-agent', user_agent)]
        
        if top_url.endswith("/"):
            self.top_url = top_url[:-1]
        self.top_url = top_url

    def url_content(self, target_url):
        ''' Retrieve URL raw Content.
        
        Keyword arguments:
        target_url -- url to inspect.
        
        '''
        
        # Get correct format of URL
        target_url = self.generate_correct_url(target_url)

        raw_code = self.opener.open(target_url)
        soup_code = Soup(raw_code)

        return soup_code

    def generate_correct_url(self, url_to_check):
        ''' Check the url and generate a new one well formed if is not complete.
            * Url management starts with '/' or /wiki/ - InvalidURL
            * Url management starts with '//' - HTTPError
            * Url format t0 utf-8 - http://es.wikipedia.org//yi.wikipedia.org/wiki/%D7%B0%D7%99%D7%A7%D7%99%D7%A4%D6%BC%D7%A2%D7%93%D7%99%D7%A2:%D7%91%D7%A8%D7%95%D7%9B%D7%99%D7%9D_%D7%94%D7%91%D7%90%D7%99%D7%9D
        
        Keyword arguments:
        url_to_check -- URL to check

        '''
        
        if url_to_check.startswith("//"):
            url_to_check = "http:" + url_to_check
        elif url_to_check.startswith("/"):
            url_to_check = self.top_url + url_to_check
        elif url_to_check.startswith("https://") or \
            url_to_check.startswith("http://"):
            url_to_check = url_to_check

        return url_to_check
