# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

assert 1 == 1

# %%
assert 1 == 2

# %%
def test_sum():
    assert sum([1, 2, 3]) == 6, 'Powinno być 6'
    
    
def test_min():
    assert min([1, 2, 3]) == 2, 'Powinno być 1'

# %%
if __name__ == '__main__':
    test_sum()
    test_min()
    print('Wszystko ok.')