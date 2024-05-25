mitupla = ("alejandra", 56, 3.14, 36.75, "Richard", 56,"Ale",56)
print(mitupla)
print(mitupla[:])
print(mitupla[1:4])

# convertir una lista a una tupla

milista = ["Ale",56,3.14159,True]
print(milista)                  # aparece con [] entonces es lista
mitupla_nueva = tuple(milista)
print(mitupla_nueva)            # aparece con () entonces es tuple

# convertir una tupla a una lista

print(mitupla)
milista = list(mitupla)
print(milista)

# buscar un elemento

print("alejandra" in mitupla)

nombre= "ALejanDra"
convertir = nombre.lower()
convertirmayuscula = nombre.upper()

print(convertir in mitupla)
print(convertirmayuscula in mitupla)

# contar la cantidad de veces que un elemento esta en la tupla

print(mitupla.count(14))
print(mitupla.count(56))
print(mitupla.count("Ale"))

# cantidad de elementos de una tupla

print(len(mitupla))

mitupla_unelemento = ("Ale",) #Tupla con SOLO 1 elemento

# en una tupla no necesito poner () - empaquetado de tupla

mitupla_sinparentesis = "alejandra", 56, 3.14, 36.75, "Richard", 56,"Ale",56
print(mitupla_sinparentesis)

# desempaquetado de una tupla (asigno a variables)

tupla_nacimiento = ("Sebastian", 17,10,1996)
nombre,dia,mes,anio = tupla_nacimiento
print (nombre)
print (dia,"/",mes,"/",anio)













