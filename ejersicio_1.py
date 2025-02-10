# desarrollar un programa que identifique si en una lista existen o no elementos repetidos
lista = ['perro','gato','cacatua','sable','nutria','uron','loro','marsupial']
lista_repetidos =[]
for i in lista:
    if lista.count(i) != 1:
        if i not in lista_repetidos:
            lista_repetidos.append(i)
if len(lista_repetidos) !=0:
    for i in lista_repetidos:
        print(f'en la lista el elemento "{i}" esta repetido un total de {lista.count(i)}')
else:
    print('no hay elementos repetidos')