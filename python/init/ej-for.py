

lista = ['manzana', 'platano', 'pera', 'frutilla', 'papaya', 'pina']
'''
    este es un documento para explicar la variable lista
'''

'''
    for (var i = 0; i < lista.length(); i+=3){
        print(lista[i])
    }

    for ( var i = -20; i <= 20; i=i+4) {
        print(i)
    }

    for(int i = 0; i < lista.lenght(); i++){
        ...
    }
'''

# -20, -16, -18, .... 20
for i in range(0, 21):
    print(i)


for i in range(len(lista)):
    if lista[i] == 'frutilla':
        lista[i] = lista[i].upper()
    
    if lista[i] == 'papaya':
        lista.append('coco')


#lista.remove('FRUTILLA')
print(lista)

# print('-------------')

# for i in lista:
#     if i == 'frutilla':
#         pass

# while 'FRUTILLA' in lista:
#     print('hola')

# # print(lista)
    