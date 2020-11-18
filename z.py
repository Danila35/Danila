def my_func(var_1, var_2):
    if var_2 != 0:
        return var_1 + var_2
    else:
        print("Вы делили на ноль")
print(my_func(int(input("Введите первое число: ")), int(input("Введите второе число: "))))