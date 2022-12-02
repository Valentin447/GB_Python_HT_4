'''
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

script_name, working_time, working_rate, bonus = argv


def salary(wt, wr, b):
    return int(wt) * int(wr) + int(b)


print(salary(wt=working_time, wr=working_rate, b=bonus))
