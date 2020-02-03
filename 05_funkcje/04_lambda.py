# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

def parabola(x):
    return x**2 + 3

print(type(parabola))

print(parabola(30))

# %%
funkcja_1 = parabola

print(funkcja_1(30))

# %%
f = lambda x: x**2 + 3
f(30)

# %%
f_2 = lambda word: word.upper()
f_2('python')

# %%
add = lambda x, y: x + y
add(3, 5)

# %%
f_4 = lambda word_1, word_2: word_1 + ' ' + word_2
f_4('Hello', 'World')

# %%

lista = ['python', 'java', 'r', 'sql']

list(map(lambda word: word.upper(), lista))

def make_upper(word):
    return word.upper()
# %%
list(map(make_upper, lista))

# %%
list(map(str.upper, lista))

# %%
list(map(lambda word: word.title(), lista))

# %%
list(map(lambda word: (word, len(word)), lista))


# %%
def apply_function(x, fn):
    return fn(x)

apply_function(5, lambda x: x**2)
apply_function([12, 42], lambda x: sum(x))

# %%
numbers = [6, 3, 1, 8, 3, 0]
sorted(numbers)

numbers = [-3, -2, -1, 0, 1, 2, 3]
sorted(numbers, key=lambda x: abs(x))

# %%
lista = [('jeden', 'one'), ('dwa', 'two'), ('trzy', 'three')]

sorted(lista)
sorted(lista, key=lambda x: x[1])

# %%
for item in lista:
    print(item)














