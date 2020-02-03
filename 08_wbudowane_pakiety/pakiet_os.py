# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import os

# %%
dir(os)

# %%
os.getcwd()

# %%
os.chdir('C:\\Users\\krako\\repos\\python_course\\08_wbudowane_pakiety')

# %%
os.getcwd()

# %%
os.system('mkdir test')

# %%
os.rmdir('dir1')

# %%
os.listdir()

# %%
for item in os.listdir():
    print(item)

# %%
for item in os.listdir():
    if item.endswith('.py'):
        print(item)

# %%
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)

# %%
os.path.join(r'home\user\bin', 'python')
