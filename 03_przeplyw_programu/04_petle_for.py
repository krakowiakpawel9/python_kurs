# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

# %%
name = 'sas'

for character in name:
    print(character)

# %%
name = 'python'
index = 0

for character in name:
    print(index, character)
    index = index + 1

# %%
for index in range(10):
    print(index)

# %%
for index in range(len(name)):
    print('Nr indeksu:', index, 'Liter:', name[index])

# %%
for i in enumerate(name):
    print(i)

# %%
for indeks, character in enumerate(name):
    print('Nr indeksu:', indeks, character)

# %%
for i in [4, 5, 6, 8, 6]:
    print(i)
# %%
for i, value in enumerate([4, 5, 6, 8, 6]):
    print(i, value)

# %%
for i in range(10):
    print(i)

# %%
for i in range(10, 20):
    print(i)

# %%
for i in range(10, -1, -1):
    print(i)

# %%
for i in range(10, 100, 10):
    print(i)

# %%
techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])


# %%
string = 'Python Course'
for char in string[:6]:
    print(char)

# %%
string = 'Python Course'
for char in string[::-1]:
    print(char)

# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    print(char)

# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)

# %%
for char in zip('abcde', '12345'):
    print(char)

# %%
for char, number in zip('abc', 'python'):
    print(char, number)

# %%

hashtags = '#sport#gym#fitness#'

result = ''
for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''








