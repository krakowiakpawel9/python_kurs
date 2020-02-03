# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

def generator():
    
    yield 4
    
    yield 5
    
# %%
gen = generator()

# %%
next(gen)

# %%
def generator_2(word):
    letters = list(word)
    for letter in letters:
        yield letter
 
gen_2 = generator_2('python')

# %%
next(gen_2)

# %%
for item in generator_2('predator'):
    print(item)
       
# %%
gen = generator_2('comp')

# %%

files = ['script_1.py', 'script_2.py', 'text.txt']

def gen_files(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item
            
gen = gen_files(files)

# %%
next(gen)

# %%
for i in gen:
    print(i)






    
    