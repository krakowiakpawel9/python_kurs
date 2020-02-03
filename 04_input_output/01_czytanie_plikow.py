# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

file = open('simple.txt', 'r')

for line in file:
    print(line, end='')

file.close()

# %%
with open('simple.txt', 'r') as file:
    for line in file:
        print(line, end='')

# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)

# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# %%
with open('simple.txt', 'r') as file:
    lines = file.read()
    print(lines)

