diccionario = {
    "nombre" : 'Andres',
    "apellido" : 'Pedraza',
    "edad" : 22 
}
#Nos devuelve un objeto dict_item
claves = diccionario.keys()

#Obteniendo un elemento con get() (No lanza excepciones)
getters = diccionario.get("nombre")

#ELIMINANDO todo del diccionario 
#diccionario.clear()

#eliminando un elemento del diccionario 

diccionario.pop("nombre","apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable =diccionario.items()
print(diccionario_iterable)