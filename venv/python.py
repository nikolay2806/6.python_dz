import math
from random import randint
from math import *

# Возвести в степень
def py_pow(a,b):
    return pow(a,b) 

# Найти корень числа
def py_sqrt(a):
    return math.sqrt(a)

# Чило pi
def py_pi(a):
    if a == math.pi:
        return True
    else:
        return False
# Найти гепотинузу треугольник
def py_hypot(a,b):
     return int(hypot(a,b))

"""
    Программа Python для фильтрации нечетных чисел
    в списке, используя функцию filter()
"""

# функция, которая проверяет числа

def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

# def out_filter(filter_odd_num,numbers):
#     return filter(filter_odd_num,numbers)

filter(filter_odd_num,numbers)
