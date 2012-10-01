# coding=UTF-8
'''
Created on 27/09/2012

@author: ricardo
'''
import urllib2
from urllib2 import _opener, HTTPError
from BeautifulSoup import BeautifulSoup as Soup
from httplib import InvalidURL
from setuptools.package_index import user_agent

class UrlContentRetrieve:

    def __init__(self, topUrl):
        '''Initializes UrlContentRetrieve with default user_agent.
        
        '''

        user_agent = "Mozilla/5.0 (X11; U; Linux x86_64; en-Us) AppleWebKit/534.7 (KHTML, Like Gecko) Chrome /7.0.517.41 Safari/534.7"

        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-agent', user_agent)]
        
        if topUrl.endswith("/"):
            self.topUrl = topUrl[:-1]
        self.topUrl = topUrl

    def urlContent(self, target_url):
        ''' Retrieve URL raw Content.
        
        Keyword arguments:
        target_url -- url to inspect.
        
        '''
        
        # Get correct format of URL
        target_url = self.generateCorrectURL(target_url)

        raw_code = self.opener.open(target_url)
        soup_code = Soup(raw_code)

        return soup_code

    def generateCorrectURL(self, urlToCheck):
        ''' Check the url and generate a new one well formed if is not complete.
            * Url management starts with '/' or /wiki/ - InvalidURL
            * Url management starts with '//' - HTTPError
            * Url format t0 utf-8 - http://es.wikipedia.org//yi.wikipedia.org/wiki/%D7%B0%D7%99%D7%A7%D7%99%D7%A4%D6%BC%D7%A2%D7%93%D7%99%D7%A2:%D7%91%D7%A8%D7%95%D7%9B%D7%99%D7%9D_%D7%94%D7%91%D7%90%D7%99%D7%9D
        
        Keyword arguments:
        urlToCheck -- URL to check

        '''
        
        if urlToCheck.startswith("//"):
            urlToCheck = "http:" + urlToCheck
        elif urlToCheck.startswith("/"):
            urlToCheck = self.topUrl + urlToCheck
        elif urlToCheck.startswith("https://") or urlToCheck.startswith("http://"):
            urlToCheck = urlToCheck

        return urlToCheck
