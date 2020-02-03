# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import datetime
import time

print(datetime.datetime.utcnow())

# %%
def log(message, dt=datetime.datetime.utcnow()):
    print(dt, message)

log('Uruchomienie systemu.')

# %%
def logi(*args):
    for command in args:
        log(command)
        time.sleep(1)

logi('Uruchomienie systemu', 'Logowanie', 'Restart', 'Wylogowanie',
     'Zamknięcie systemu')