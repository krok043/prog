from math import factorial
from tkinter import N
from typing import Tuple


a = int(input())
b = int(input())

es_mul = False

if a >= b:
    if a % b == 0:
        es_mul = True
    # else:
    #     es_mul = False
else:
    if b % a == 0:
        es_mul = True
    # else:
    #     es_mul = False
print('Es multiplo') if es_mul else print('No es multiplo')