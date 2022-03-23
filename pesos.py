casos_de_prueba =  int(input())
#casos_de_prueba = 3
for contador in range(0, casos_de_prueba):
    peso_lulu = int(input())
    peso_leliz = int(input())
    cantidad_anios = 0

    #peso_lulu = 4
    #peso_leliz = 7

    while peso_lulu <= peso_leliz:
        cantidad_anios = cantidad_anios + 1
        peso_lulu = peso_lulu * 3
        peso_leliz = peso_leliz * 2

    print(cantidad_anios)