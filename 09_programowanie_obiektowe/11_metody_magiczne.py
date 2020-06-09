# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""
   
# %%
1 + 1

# %%
type(1)

# %%
dir(int)

# %%
int.__add__(1, 2)

# %%
int.__sub__(10, 7)

# %%
"""
Operatory:
    +  : __add__(self, other)
    -  : __sub__(self, other)
    *  : __mul__(self, other)
    /  : __truediv__(self, other)
    // : __floordiv__(self, other)
    %  : __mod__(self, other)
    ** : __pow__(self, other)

Operatory Porównawcze:
    <  : __lt__(self, other)
    >  : __gt__(self, other)
    <= : __le__(self, other)
    >= : __ge__(self, other)
    == : __eq__(self, other)
    != : __ne__(self, other)
"""
int.__lt__(3, 6)

# %%

class SpecialInt(int):
    
    def __init__(self, special_int):
        self.special_int = special_int
        
    def __add__(self, other):
        return self.special_int + other.special_int + 10
    
    def __sub__(self, other):
        return self.special_int - other.special_int - 10
    
# %%
s_1 = SpecialInt(2)
s_2 = SpecialInt(3)

s_1 + s_2

# %%
s_1 - s_2

# %%
class Kwadrat:
    
    def __init__(self, dlugosc_boku):
        self.dlugosc_boku = dlugosc_boku
        
    def __str__(self):
        return f"Kwadrat o boku {self.dlugosc_boku}cm."
    
    def pole(self):
        return self.dlugosc_boku ** 2
    
    def __add__(self, other):
        return self.pole() + other.pole()
    
    def __sub__(self, other):
        return self.pole() - other.pole()
    
    def __lt__(self, other):
        return self.pole() < other.pole()
        
# %%
k1 = Kwadrat(3)
k2 = Kwadrat(10)

# %%
k1.pole()

# %%
print(k1)
print(k2)

# %%
k1 + k2

# %%
k1 - k2

# %%
k1 < k2

# %%











