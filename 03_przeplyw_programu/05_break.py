# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

# %%
for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        break

print('Koniec')

# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        break
    print(char)

print('Koniec')

# %%
for char in 'kowalskijgmail.com':
    if char == '@':
        print('Adres email zweryfikowany.')
        break
else:
    print('Adres email nie jest poprawny')


print('Koniec')
