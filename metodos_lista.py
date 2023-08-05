#Creando una lista con list 
lista = list(["hola","Andres",22])

#devolver cantidad de elemntos en la lista
cantidad_elementos = len(lista)

#agregando un alemento a la lista
lista.append("JAJAJA")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"TOMA MAMA")

#agregando varios elementos a la lista
lista.extend([False,2022])

#eliminando un elemento de la lista (por su indice)
#lista.pop(-1) Se elimina el ultimo elemento de la lista
lista.pop(0)

#remueve un elemento de la lista por su valor
lista.remove("TOMA MAMA")

#eliminando todos los elemetos de la lista 
lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa )
#list.sort(reverse=True)
list.sort()

#invirtiendo los elementos de una lista 
lista.reverse()

print(lista)
