numero = int(input("Ingresa un número entero positivo: "))
contador = 1

while contador <= numero:
    print(contador, end=" ")
    contador += 1

contador -= 2

while contador >= 1:
    print(contador, end=" ")
    contador -= 1
