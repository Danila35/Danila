def step(a, b):
    c = 1
    for i in range(abs(b)):
        c *= a
    if b >= 0:
        return c
    else:
        return 1 / c
 
 
print(step(float(input("Первое значение - ")), int(input("Второе значение - "))))