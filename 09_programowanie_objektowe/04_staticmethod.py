# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

class Student:

    lista_studentow = []

    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_studentow.append(self)

    @staticmethod
    def liczba_studentow():
        print('Liczba studentów:', len(Student.lista_studentow))

# %%
student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('Tomasz', 'Nowak', 23)
student_3 = Student('Jan', 'Nowak', 20)

# %%
Student.liczba_studentow()
