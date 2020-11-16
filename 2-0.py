my_list = int(input("Введите количество элементов списка "))
new_list = []
a = 0
el = 0
while a < my_list:
    new_list.append(input("Введите следующее значение списка "))
    a += 1

for el in range(int(len(new_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)