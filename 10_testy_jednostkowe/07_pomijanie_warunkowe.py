# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

"""
Opis metod:
    
    unittest.skip(reason)
        pomija oznaczony test
    
    unittest.skipIf(condition, reason)
        pomija oznaczony test jeżeli warunek jest prawdziwy
        
    unittest.skipUnless(condition, reason)
        pomija oznaczony test, chyba, że warunek jest prawdziwy
        
    unittest.expectedFailure()
        oznacza test jako oczekiwany błąd, jeżeli test będzie niepowodzeniem
        nie zostanie policzony jako błąd.
"""
import unittest


class SimpleTest(unittest.TestCase):
    
    x = 6
    y = 8
    
    @unittest.skip('Pomin')
    def test_add(self):
        wynik = self.x + self.y
        self.assertEqual(wynik, 6)
    
    @unittest.skipIf(x < y, 'Pomin')
    def test_sub(self):
        wynik = self.x - self.y
        self.assertEqual(wynik, 2)
    
    @unittest.skipUnless(y == 0, 'Pomin')
    def test_div(self):
        wynik = self.x / self.y
        self.assertEqual(wynik, 3.0)
        
    @unittest.expectedFailure
    def test_mul(self):
        wynik = self.x * self.y
        self.assertEqual(wynik, 10)


if __name__ == '__main__':
    unittest.main()    
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
