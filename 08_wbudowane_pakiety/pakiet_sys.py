# -*- coding: utf-8 -*-

import sys

print(sys.argv)

args = sys.argv

print('Nazwa pliku:', args.pop(0))

i = 1
while args:
    print('Argument nr {}: {}'.format(i, args.pop(0)))
    i += 1