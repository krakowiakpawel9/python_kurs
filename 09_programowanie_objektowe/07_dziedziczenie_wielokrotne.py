# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'Jack'
    

class Polak:
    
    kraj = 'Polska'
    # imie = 'Piotr'
    
    
class Pilkarz(Polak, Czlowiek):
    
    def info(self):
        print(f'Utworzony obiekt pochodzi z planety {self.pochodzenie}.\n'
              f'Kraj pochodzenia: {self.kraj}.\n'
              f'Nazwa obiektu: {self.imie}')
        
# %%
pilkarz_1 = Pilkarz()
pilkarz_1.info()
    