# Crear una lista de 5 numeros al azar entre el 0 y el 9
# que esten ordenados y no repetidos

import random # esto genera el numeros al azar
lista =[]
numero = random.randint(0,45)
while len(lista) < 5 :              # lista de cinco numeros (elementos)
    if numero not in lista:         # me aseguro que no esten repetidos
        lista.append(numero)
    numero = random.randint(0,45)

lista.sort()                        # ordenados de menor a mayor
print(lista)

