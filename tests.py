# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import unittest
from autocomplete import main

class AutocompleteTestCase(unittest.TestCase):

    def setUp(self):
        self.instance = main.Autocomplete()

    def tearDown(self):
        pass

    
    def test_native_substring_search(self):
        self.assertEqual( main.native_substring_search("ABC ABCDAB ABCDABCDABDE", "ABCDABD") , [15])
        self.assertEqual(main.native_substring_search("ABC ABCDAB ABCDABCDABDE", "ABC"), [0, 4, 11, 15])
       


if __name__ == '__main__':
    unittest.main()



