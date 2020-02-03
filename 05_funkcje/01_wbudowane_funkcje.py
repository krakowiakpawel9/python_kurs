# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

# %%
print(abs(10))
print(abs(-10))

# %%
bool([])
bool('')
bool({})
bool(' ')
bool(True)
bool(False)
bool(12)
bool(0)

# %%
dir(list)
dir(tuple)

# %%
list(enumerate(['pawel', 'python', 'java']))

# %%
eval('1 + 1')

x = 10
eval('x + 13')

# %%

list(filter(abs, [-2, -1, 0, 1, 2]))

# %%
list(filter(bool, ['python', '', 'java']))

# %%
float(1)
float(1.3)
float('1')
float('3.5')

# %%
type(1)
type('vdf')

# %%
help(float)
help(int)

# %%
isinstance(1, int)
isinstance(1.0, float)
isinstance('', str)

# %%
len('python')
len('')
len(' ')
len([])
len([[3, 4], [4, 5, 6, 7, [5, 5]]])

# %%
list('pytohn')
list(range(10))


# %%
list(map(abs, [-2, -1, 0, 1, 2]))

# %%
names = ['pawel', 'tomek', 'janek']
list(map(str.title, names))

# %%
max([1, 2, 5, 2])
max('pawel')
max('tomek')

min([1, 2, 4, 6])
min('pawel')
min('tomek')

# %%
pow(2, 4)
2 ** 4

# %%
list(reversed([5, 3, 7]))
list(reversed('python'))

# %%
round(4.32435342, 2)

# %%
str(1)
str(343.434)

# %%
sum([3, 4, 5, 3])

# %%
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6, 5]

list(zip(lista_1, lista_2))

# %%
list(zip('python', 'coursedsdsd'))










