# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

class A:
    
    def metoda(self):
        print('Metoda z klasy A')
        
class B(A):
    
    pass

class C(A):
    
    pass

class D(B, C):
    
    pass
        
# %%
d = D()
d.metoda()        