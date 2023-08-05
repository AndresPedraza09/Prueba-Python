diccionario = {
    "Nombre":"Andres",
    "Apellido": "Pedraza",
    "Edad": 22
}

#print(diccionario)

#Recorriendo diccionario para obtener las claves
for key in diccionario.items():
    print(key)

#Recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} El valor es: {value}")