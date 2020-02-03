# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

text = 'Witaj na kursie Pythona.\nPython jest wspaniały.'

print(text)

# %%
dir(text)
help(str.count)

# %%
text.capitalize()

# %%
text.title()

# %%
text.count('Python')

# %%
text.startswith('kurs')

# %%
'python'.startswith('py')

# %%
text.endswith('y.')

# %%
'sample.txt'.endswith('.py')

# %%
'sample.png'.endswith('.png')

# %%
text.find('Python')
text[text.find('Python'):]

# %%
hashtags = 'sport#gym'
idx = hashtags.find('#')
hashtags[:idx]

# %%
'pawel545'.isalnum()

# %%
'43434fvd'.isdigit()

# %%
'pyThon'.islower()

'PAWEL'.isupper()

# %%
' '.join(['python', '3.7'])
'#'.join(['sport', 'gym', 'fit'])
','.join(['1', '2', '3', '4'])

# %%
'#good#time#mood'.replace('#', ' ')

# %%
'column name'.replace(' ', '_')

# %%
'    python   '.strip()
'    python   '.rstrip()
'    python   '.lstrip()

# %%
'1,2,3,4,5'.split(',')

'python java php sql sas'.split()

'#gym#fit#mood'.split('#')

# %%
'12'.zfill(5)
'1'.zfill(10)











