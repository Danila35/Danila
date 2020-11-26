slova = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
n_f = []
with open('4-0.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        n_f.append(slova[i[0]] + '  ' + i[1])
    print(n_f)

with open('4-n.txt', 'w') as file_obj_2:
    file_obj_2.writelines(n_f)