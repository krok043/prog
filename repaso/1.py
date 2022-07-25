cad = input()

# cantidad_elementos = len(cad) * (-1) - 1

# for i in range(-1, cantidad_elementos, -1):
#     print(cad[i], end='')

can_ele = len(cad) - 1
print()

for i in range(can_ele, -1, -1):
    print(cad[i], end='')