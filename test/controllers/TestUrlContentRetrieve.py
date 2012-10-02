'''
Created on 01/10/2012

@author: ricardo
'''
import unittest
from controllers.url_content_retrieve import UrlContentRetrieve
from urllib2 import URLError

class TestUrlContentRetrieve(unittest.TestCase):
    '''Test class for methods defined in UrlContentRetrieve class.
    '''

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_generate_correct_url(self):
        ''' Test method for retrieve the correct URL
        '''
        
        starting_url = "http://localhost"
        url_content_retrieve = UrlContentRetrieve(starting_url)

        # Test 1
        url_to_check = "http://localhost"
        expected_url = "http://localhost"
        returned_url = url_content_retrieve.generate_correct_url(url_to_check)
        
        self.assertEqual(returned_url, expected_url, \
                         "Error converting URL\n:\t* from: "\
                          + url_to_check + "\n\t* to: " + expected_url + \
                          "\nReturned value: " + returned_url)

        # Test 2    
        url_to_check = "/media"
        expected_url = "http://localhost/media"
        returned_url = url_content_retrieve.generate_correct_url(url_to_check)
        
        self.assertEqual(returned_url, expected_url, \
                         "Error converting URL\n:\t* from: "\
                          + url_to_check + "\n\t* to: " + expected_url + \
                          "\nReturned value: " + returned_url)

        # Test 3
        url_to_check = "//mediateca.org"
        expected_url = "http://mediateca.org"
        returned_url = url_content_retrieve.generate_correct_url(url_to_check)
        
        self.assertEqual(returned_url, expected_url, \
                         "Error converting URL\n:\t* from: "\
                          + url_to_check + "\n\t* to: " + expected_url + \
                          "\nReturned value: " + returned_url)
        
    def test_url_content(self):
        '''Test method for retrieve content from url.
        '''
        
        # Initialize object
        starting_url = "http://non-existing-url.com"
        url_content_retrieve = UrlContentRetrieve(starting_url)

        # Test 1 - Variables
        # Return error
        target_url = "http://non-existing-url.com"
        expected_exception = \
            "<urlopen error [Errno -2] Name or service not known>"
        try:
            returned_soup_code = url_content_retrieve.url_content(target_url)
            self.assertIsNone(returned_soup_code, \
                              "Url content has return a value:\n"\
                              + str(returned_soup_code))
        except URLError, url_error:
            self.assertEqual(expected_exception, str(url_error), "Exception "\
                             "URLError is not correct with message:\n"\
                             + str(url_error))
        
        # Test 2 - enconding
        starting_url = "http://es.wikipedia.org"
        url_content_retrieve = UrlContentRetrieve(starting_url)
        target_url = \
            "http://es.wikipedia.org/wiki/Depresi%C3%B3n_tropical_Diez_(2007)"
        expected_enconding = "utf-8"
        
        returned_soup_code = url_content_retrieve.url_content(target_url)
        
        returned_enconding = returned_soup_code.originalEncoding

        self.assertEqual(expected_enconding, returned_enconding, \
                         "Encondin doesn't match:\n\t* Expected: "\
                         + expected_enconding + "\n\t* Returned: "\
                         + returned_enconding)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
