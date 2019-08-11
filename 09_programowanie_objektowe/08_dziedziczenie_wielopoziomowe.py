# -*- coding: utf-8 -*-

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    # imie = 'Jack'
    

class Polak(Czlowiek):
    
    kraj = 'Polska'
    # imie = 'Piotr'
    

class Programista(Polak):
    
    technologia = 'Python'
    # imie = 'Krzysztof'
    
    def info(self):
        print(f'Pochodzenie: {self.pochodzenie}\n'
              f'Kraj: {self.kraj}\n'
              f'Technologia: {self.technologia}\n'
              f'Imie: {self.imie}')
        
# %%
programista_1 = Programista()
programista_1.info()