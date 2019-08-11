# -*- coding: utf-8 -*-

KOD_PIN = '0000'

pin = input('Podaj kod pin: ')

while pin != KOD_PIN:
    pin = input('Sproboj ponownie jeszcze raz: ')

print('Zalogowany!')

# %%
KOD_PIN = '0000'

pin = ''
counter = 0

while pin != KOD_PIN and counter < 3:
    pin = input('Wprowadz kod pin: ')
    if pin == KOD_PIN:
        print('Zalogowany')
        break
    counter += 1
else:
    print('Zbyt dużo prób logowania.')
