from sys import argv

wage, time, earn, bonus = argv
try:
    time = int(time)
    earn = int(earn)
    bonus = int(bonus)
    wage = time * earn + bonus
    print(f'заработная плата сотрудника  {wage}')
except ValueError:
    print('Недостоточно данных')