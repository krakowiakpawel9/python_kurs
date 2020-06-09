# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

class Czlowiek:
    
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        
    def info(self):
        print(f'{self.imie} {self.nazwisko}')
      
        
class Pilkarz(Czlowiek):
    
    def __init__(self, imie, nazwisko, klub):
        super().__init__(imie, nazwisko)
        self.klub = klub
        
    def info(self):
        super().info()
        print(f'Klub: {self.klub}')
        
# %%
pilkarz_1 = Pilkarz('Robert', 'Lewandowski', 'Bayern') 
pilkarz_2 = Pilkarz('Krzysztof', 'Piątek', 'AC Milan')

# %%
pilkarz_1.info() 
pilkarz_2.info() 

        
    
        
        
    
        
        