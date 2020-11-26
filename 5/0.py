def summary():
    try:
        with open('5-0.txt', 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка в файле.')
    except ValueError:
        print('Неправильно набран номер.')
summary()