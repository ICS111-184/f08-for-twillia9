# -*- coding: utf-8 -*-
"""
Table with a column for decimal, binary, and hexidecimal
"""

x = 0
print('decimal\t\tbinary\t\thex')

for x in range(8):
    print(x, '\t', '\t', bin(x), '\t', '\t', hex(x))
    #extra tab for lower numbers
for x in range(8,32):
    print(x, '\t', '\t', bin(x), '\t', hex(x))
