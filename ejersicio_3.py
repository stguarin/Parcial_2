#desarrollar un programa que dadas 2 listas determine que elementos tiene la primera lista que la segunda 
# lista no tenga
lista_1 = [1,2,3,4,5,6,7,8,9]
lista_2 = [2,4,6,8,10]
for i in range(len(lista_1)):
    if lista_1[i] not in lista_2:
        print(f'el elemento "{lista_1[i]}" no esta en la lista 2')
    