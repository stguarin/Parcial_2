#desarrollar un programa que determine si en una lista se encuentra una cadena con 2 o mas vocales. si la cadena 
# si la cadena existe debe imprimirla y si no existe debe imprimir no existen

lista = ['qqq','www','rrr','ttt','yyy']
punto =0
for i in lista:
    contador =0
    for x in i:
        contador = contador +i.count('a')+i.count('e')+i.count('i')+i.count('o')+i.count('u')
        if contador >=2:
            print(f'la palabra {i} tiene 2 vocales o mas')
            punto=1
            break
if punto ==0:
    print('no existe una cadena con 2 o mas vcales')