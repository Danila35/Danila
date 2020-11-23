from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el > 10:
        break
    else:
        print(el)


from itertools import cycle
c = 0
for el in cycle(['ABC', False, 123]):
    if c > 10:
        break
    print(el)
    c += 1
