# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc', 'UBER.US': 'Uber Technologies Inc',
          'MSFT.US': 'Microsoft Corp'}
# %%
{key: 'Corp' if 'Corp' in val else 'Inc' for (key, val) in stocks.items()}

# %%
numbers = range(20)
numbers_dict = {}

for n in numbers:
    if n % 2 == 0:
        numbers_dict[n] = n ** 2
print(numbers_dict)

# %%
num_dict = {key: key ** 2 for key in numbers if key % 2 == 0}

# %%
nested_dict = {'001': {'price': 100},
               '002': {'price': 40},
               '003': {'price': 60}}

for key, val in nested_dict.items():
    print(key, val)

# %%
{key:val['price'] for (key, val) in nested_dict.items()}

# %%
nested_dict = {'001': {'price': 100, 'items': 4},
               '003': {'price': 60, 'items': 8}}

# %%
for key, val in nested_dict.items():
    print(key, val)

# %%
{key:val['price'] for (key, val) in nested_dict.items()}
{key: val['price'] * val['items'] for (key, val) in nested_dict.items()}