#Ingresa un numero por teclado y suma los digitos de ese mismo

#1. numero -> str

#2. numero -> int

numero = input("Ingresa numero: ")
suma = 0
for i in range(0, len(numero)):
    suma = suma + int(numero[i])
print(suma)
