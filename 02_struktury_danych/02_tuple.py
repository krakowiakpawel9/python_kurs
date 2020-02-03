# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)

# %%
name_google = google[0]

# %%
data = (amazon, google)
print(data)

# %%
a = ('Pawel', 'Krakowiak')
print(a)

# %%
imie = 'Pawel'
nazwisko = 'Krakowiak'

# %%
imie, nazwisko, id_user = ('Pawel', 'Krakowiak', '001')

# %%
amazon_name, country, sector, rank = amazon

# %%
stocks = 'Amazon', 'Apple', 'IBM'

print(type(stocks))

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Krakow', 'Wroclaw')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c
print(a, b)

# %%
x, y = 10, 15
x, y = y, x
print(x, y)










