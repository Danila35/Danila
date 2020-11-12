revenue = int(input("Введите выручку "))
cost = int(input("Введите издержки "))

if revenue > cost:
	print("Ваш финансовый результат прибыльный")
	ratio = revenue / cost
	print("Соотношение равно: " + str(ratio))
else:
	print("Ваш финансовый результат убыточный")
a = int(input("Введите число сотрудников "))
b = revenue / a
print("Прибыл на одного работника:" + str(b)) 




