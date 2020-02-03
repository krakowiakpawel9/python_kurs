# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

def add(x, y):
    """Zwraca sumę dwóch liczb.
    
    >>> add(3, 4)
    7
    
    >>> add(2, 8)
    100
    """
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testfile('test.txt')