'''
Created on 01/10/2012

@author: ricardo
'''
import unittest
from url_content_retrieve import UrlContentRetrieve


class TestUrlContentRetrieve(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGenerateCorrectURL(self):
        ''' Test method for retrieve the correct URL
        
        '''
        
        startingURL = "http://localhost"
        urlContentRetrieve = UrlContentRetrieve(startingURL)

        # Test 1
        urlToCheck = "http://localhost"
        expectedURL = "http://localhost"
        returnedURL = urlContentRetrieve.generateCorrectURL(urlToCheck)
        
        self.assertEqual(returnedURL, expectedURL, "Error converting URL\n:\t* from: " + urlToCheck + "\n\t* to: " + expectedURL + "\nReturned value: " + returnedURL)

        # Test 2    
        urlToCheck = "/media"
        expectedURL = "http://localhost/media"
        returnedURL = urlContentRetrieve.generateCorrectURL(urlToCheck)
        
        self.assertEqual(returnedURL, expectedURL, "Error converting URL\n:\t* from: " + urlToCheck + "\n\t* to: " + expectedURL + "\nReturned value: " + returnedURL)

        # Test 3
        urlToCheck = "//mediateca.org"
        expectedURL = "http://mediateca.org"
        returnedURL = urlContentRetrieve.generateCorrectURL(urlToCheck)
        
        self.assertEqual(returnedURL, expectedURL, "Error converting URL\n:\t* from: " + urlToCheck + "\n\t* to: " + expectedURL + "\nReturned value: " + returnedURL)
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
