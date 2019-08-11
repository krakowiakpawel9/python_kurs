# -*- coding: utf-8 -*-

# %%
text = 'Python jest wspaniały. Python jest elastyczny. Python rządzi.'

words = text.lower().replace('.', '').split()

unique_words = {word for word in words}
print(unique_words)

# %%
unique_words_gt_4 = {word for word in words if len(word) > 4}
print(unique_words_gt_4)

# %%
{word.capitalize() if word.startswith('py') else word for word in words}
