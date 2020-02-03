# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

"""
assertListEqual - sprawdza czy dwie listy są równe
assertTupleEqual - sprawdza czy dwie tuple są równe
assertSetEqual - sprawdza czy dwa zbiory są równe
assertDictEqual - sprawdza czy dwa słowniki są równe
"""

import unittest


class SimpleTest(unittest.TestCase):
    
    def test_1(self):
        self.assertListEqual([1, 2, 4], [1, 2, 3])
        
    def test_2(self):
        self.assertTupleEqual((1, 3), (1, 2))
        
    def test_3(self):
        self.assertSetEqual({4, 2}, {4, 5})
        
    def test_4(self):
        self.assertDictEqual({'a': 2, 'b': 2}, {'a': 1, 'b': 2})
        
    
if __name__ == '__main__':
    unittest.main()