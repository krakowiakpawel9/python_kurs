# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

# %%
techs = []
print(techs)

# %%
techs.append('python')
print(techs)

# %%
techs.append('java')

# %%
techs.append(['hadoop', 'spark'])
print(techs)

# %%
techs.extend(['sql', 'sas'])
print(techs)

# %%
techs.insert(0, 'go')
print(techs)

# %%
techs.insert(2, 'r')
print(techs)

# %%
print(techs)
print(techs.pop())
print(techs)

# %%
# techs = ['python', 'java', 'sql', 'php']
print(techs.pop(0))
print(techs)

# %%
techs = ['python', 'java', 'sql', 'php']

techs.index('java')
# techs.index('jav')

# %%

techs = ['python', 'java', 'sql', 'php', 'python']
techs.count('python')
techs.count('jav')

# %%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs.sort(reverse=True)
print(techs)

# %%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
# techs[::-1]
techs.reverse()
print(techs)

# %%
techs[1] = 'c++'
print(techs)









