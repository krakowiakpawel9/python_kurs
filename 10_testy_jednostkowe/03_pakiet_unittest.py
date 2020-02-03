# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

"""
tworzenie testu jednostkowego 
1. zaimportowanie unittest
2. zdefiniowanie funkcji do testowania
3. stworzenie przypadku testowego użwyając klasy unittest.TestCase
4. zdefiniowanie testu jako metody klasy TestCase
5. call assert function 
6. assert function wywoła błąd assertionError jeżeli otrzymamy blad
7. wywolaj funkcje main() z modulu unittest
"""

import unittest


def add(x, y):
    return x + y


class SimpleTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(3, 4), 6, msg='Powinno być 7')
        

if __name__ == '__main__':
    unittest.main()

