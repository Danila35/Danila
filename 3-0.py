s_list = ['Январь', 'Февраль', 'Март', 'Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
s_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
m = int(input("Введите месяц по номеру: "))
if m == 12 or m == 1 or m == 2:
	if m == 12:
		print(s_list[11])
	elif m == 1:
		print(s_list[0])
	elif m == 2:
		print(s_list[1])
	print(s_dict.get(1))
elif m == 3 or m == 4 or m ==5:
	if m == 3:
		print(s_list[2])
	elif m == 4:
		print(s_list[3])
	elif m == 5:
		print(s_list[4])
	print(s_dict.get(2))
elif m == 6 or m == 7 or m == 8:
	if m == 6:
		print(s_list[5])
	elif m == 7:
		print(s_list[6])
	elif m == 8:
		print(s_list[7])
	print(s_dict.get(3))
elif m == 9 or m == 10 or m == 11:
	if m == 9:
		print(s_list[8])
	elif m == 10:
		print(s_list[9])
	elif m == 11:
		print(s_list[10])
	print(s_dict.get(4))
else:
	print("Этого месяца не существует")