f = open('text.txt', 'r')
content = f.read()
print(f'В данном файле: \n {content}')
my_f = open('text.txt', 'r')
content = my_f.readlines()
print(f'Кол-во строк - {len(content)}')
my_f = open('text.txt', 'r')
content = my_f.readlines()
for i in range(len(content)):
    print(f'Кол-во символов {i + 1} - ой строки {len(content[i])}')
my_f = open('text.txt', 'r')
content = my_f.read()
content = content.split()
print(f'Кол-во слов - {len(content)}')
my_f.close()