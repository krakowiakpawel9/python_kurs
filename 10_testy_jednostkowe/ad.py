# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

def add(x, y):
    """Zwraca sumę dwóch liczb.
    
    >>> add(4, 5)
    9
    >>> add(2, 4)
    6
    >>> add(10, 13)
    23
    >>> add(19, 1)
    20
    """
    return x + y

def load_tests(loader, tests, ignore):
   tests.addTests(doctest.DocTestSuite(ad.add))
   return tests

if __name__ == '__main__':
    import doctest
    doctest.testmod()
