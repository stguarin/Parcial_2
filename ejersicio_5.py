#desarrollar un algoritmo que determine la mediana de un arreglo de enteros (la mediana es el numero que queda en la mitad del arreglo 
# despues de ser ordenado)
arreglo_de_reales = [1,9,2,8,3,7,4,6,5]
arreglo_de_reales = sorted(arreglo_de_reales)
print(f'la mediana de el arreglo de reales es {arreglo_de_reales[len(arreglo_de_reales)//2]}')