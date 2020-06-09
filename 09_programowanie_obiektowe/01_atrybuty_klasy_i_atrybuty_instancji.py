# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

class Drzewo:

    nazwa = 'Sosna'
    wiek = 40
    wysokosc = 25


drzewo_1 = Drzewo()
drzewo_2 = Drzewo()

# %%
print(id(drzewo_1))
print(id(drzewo_2))

# %%
dir(drzewo_1)

# %%
drzewo_1.nazwa
drzewo_1.wiek
drzewo_1.wysokosc

# %%
drzewo_2.nazwa
drzewo_2.wiek

# %%
drzewo_1.stan = 'dobry'

print(dir(drzewo_2))

# %%
Drzewo.miejsce = 'las'

# %%
# print(dir(drzewo_2))
# print(drzewo_2.miejsce)

drzewo_2.miejsce = 'park'

print(drzewo_2.miejsce)














