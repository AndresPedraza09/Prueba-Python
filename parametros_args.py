def suma(nombre, *numeros):
    return f"{nombre}, la suma de los numeros es: {sum(numeros)}"

resultado = suma ("Andres",1,2,3,4,5)
print(resultado)