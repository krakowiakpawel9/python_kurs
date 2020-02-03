# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

print('Program uruchomiony...')
print("""Włam się do systemu, zgadując dwucyfrowy pin.
Numer pin składa się z cyfr: 0, 1, 2.""")
pin = input('Wprowadź numer pin: ')

if pin == '21':
    print('Brawo! Złamałes system.')
elif pin == '20':
    print('Byles blisko!')
else:
    print('Nie zgadłes.')

# %%
pin = int(input('Wprowadź numer pin: '))

if pin == 21:
    print('Brawo! Złamałes system.')
elif pin == 20:
    print('Byles blisko!')
else:
    print('Nie zgadłes.')

# %%
bool('')

# %%
string = ' '

if string:
    print('Niepusty ciąg znaków')
else:
    print('Pusty ciąg znaków')

# %%
number = 12

if number:
    print('Liczba niezerowa!')
else:
    print('Zerrrrro!!')

# %%
default_flag = False

if default_flag:
    print('Doszło do defaultu.')
else:
    print('Nie doszło')

# %%
default_flag = True

if not default_flag:
    print('Nie doszło')
else:
    print('Doszło do defaultu.')

# %%
saldo = 10000
klient_zweryfikowany = True

amount = int(input('Ile chcesz wyplacic gotowki: '))
if saldo > 0 and klient_zweryfikowany and (saldo - amount) > 0:
    print('Mozesz wyplacic gotowke')
else:
    print('Nie mozesz wyplacic gotowki. '
          'Brak wystarczajacej kwoty {}'.format(abs(saldo-amount)))

# %%

name = 'ython'

if 'p' in name:
    print('Znaleziono p')
else:
    print('Nie znalezino p')

# %%
tech = 'python'
if tech == 'python':
    flag = 'Dobry wybór'
else:
    flag = 'Poszukaj czegos lepszego.'

# %%
# x if [warunek] else y
tech = 'sas'
'Dobry wybór' if tech == 'python' else 'Poszukaj czegos lepszego'

























