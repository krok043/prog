numero = int(input("Ingresa numero: "))
suma = 0

while numero != 0:
    digito = int(numero % 10)
    numero = int(numero / 10)
    suma = suma + digito
print(suma)