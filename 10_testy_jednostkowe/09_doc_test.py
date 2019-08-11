# -*- coding: utf-8 -*-

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