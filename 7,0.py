from itertools import count
from math import factorial

def sp():
    for el in count(1):
        yield factorial(el)

gn = sp()
x = 0
for i in gn:
    if x < 10:
        print(i)
        x += 1
    else:
        break