#Creando Listas
lista = ["Andres","Pedraza",True,1.75]
#print(lista[0])

#Modificando la Lista
lista[3]= "Maquinola"
#print(lista[3])

"No se puede modificar las tuplas"
tupla = ["Andres","Pedraza",True,1.75]
#print(tupla[0])

#Creando un conjunto (sett)
#Son como las listas pero no se pueden modificar, pero si redifinirlo
#No deja repetir valores
conjunto = {"Andres","Pedraza",True,1.75}

#Creando Diccionario (dict)
diccionario = {
    'Nombre' : "Andres",
    'Apellido' : "Pedraza",
    'Es feliz' : False,
    'Altura' : 1.75
}
print(diccionario['Nombre'])
