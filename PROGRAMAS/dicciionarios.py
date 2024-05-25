
mi_diccionario = {"Nombre":"alejandra","Edad":56,"Ciudad":"Agua de Oro"}
for clave in mi_diccionario:            # devuelve las claves
    print(clave)

for valor in mi_diccionario.values():   # devuelve los valores
    print(valor)

dicc_ciudades={"Alemania":"Berlin","Fracia":"Paris","Inglaterra":"Londres", "España": "Madrid"}
print(dicc_ciudades)
print(dicc_ciudades["Alemania"])

# Agregar una clave-valor 

dicc_ciudades["Italia"]="Lisboa"
print(dicc_ciudades)

# Modificar un valor

dicc_ciudades["Italia"]="Roma"
print(dicc_ciudades)

# Borrar un elemento

print(dicc_ciudades)
del dicc_ciudades["Inglaterra"]
print(dicc_ciudades)

dicc_otrosvalores ={"Alemania":"Berlin", 23:"Jordan","alejandra":56}
print(dicc_otrosvalores)

