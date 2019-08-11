# -*- coding: utf-8 -*-
import sys


class Magazyn:

    def __init__(self, lista_produktow):
        self.lista_produktow = lista_produktow

    def wyswietl_dostepne_produkty(self):
        print('Dostępne produkty:')
        for produkt in self.lista_produktow:
            print(produkt)

    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktu: >>> ')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
        print(f'Produkt {self.nazwa_produktu} został dodany do magazynu.')

    def usun_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktu, który chcesz '
                                    'usunąć: >>> ')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print('Usunięto produkt z magazynu.')
        else:
            print('Podanego produktu nie ma na magazynie.')


# %%
magazyn = Magazyn(['mleko', 'woda', 'jajka'])

while True:
    print('Wprowadź 1 aby wyswietlić stan magaznu.')
    print('Wprowadź 2 aby dodać produkt.')
    print('Wprowadź 3 aby usunąć produkt.')
    print('Wprowadź 4 aby zakończyć.')
    wybor_uzytkownika = int(input('>>> '))
    if wybor_uzytkownika is 1:
        magazyn.wyswietl_dostepne_produkty()
    elif wybor_uzytkownika is 2:
        magazyn.dodaj_produkt()
    elif wybor_uzytkownika is 3:
        magazyn.usun_produkt()
    elif wybor_uzytkownika is 4:
        sys.exit()











