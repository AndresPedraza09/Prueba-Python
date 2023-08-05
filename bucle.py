animales = ["gato","Perro","loro","cocodrilo"]
numeros = [1,2,3,4,5,6,7,8,9,10]

#for animal in animales:
#    print(animal)

#for numero in numeros:
#   print(numero)
#Dos listas en un for usando zip (debe tener la misma cantidad de elementos)

#for numero, animal in zip (animales, numeros):
#   print(f"Recorrido lista 1: {numero}")
#  print(f"Recorrido lista 2: {animal}")

for num in range(0,10):
    print(num)

#forma no optima de recorer una lista con su indice
for num in range (len(numeros)):
    print(numeros[num])

#Forma optima de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')

#Usando el else

for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")

else:
    print("El bucle termino")