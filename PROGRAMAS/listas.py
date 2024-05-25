lista_nombres = ["Juan","Alicia","Maria","Leticia"]
print(lista_nombres)
print(lista_nombres[0])
print(lista_nombres[3])
print(lista_nombres[-1]) # me trae el ultimo
lista_nombres.append("Nahuel") # agrego un elemento
print(lista_nombres)
lista_nombres.append("Jose")
print(lista_nombres)
lista_nombres.pop(2) # elimino a Maria
print(lista_nombres)
lista_nombres.pop() # elimino el ultimo
print(lista_nombres)
lista_nombres.sort() # ordena la lista alfabeticamente
print(lista_nombres)
lista_nombres.sort(reverse=1) # ordena de mayor a menor
print(lista_nombres)

lista_notas = [1,3,8,6,4,2]
print(lista_notas)
lista_notas.sort()
print(lista_notas)
lista_notas.sort(reverse=1)
print(lista_notas)

lista_ejemplo = ["Ale",56,3.14159,True]
print(lista_ejemplo)
print(lista_ejemplo[:]) # para porciones
print(lista_ejemplo[2]) # muestra 3.14

lista_grande = ["Ale",56,3.14159,True,"cuyen",21,"julian",False]
print(lista_grande[1:6]) # no incluye la sexta posicion y genera una nueva lista
print(lista_grande[2:-1]) #-1 indica el final
lista_grande.append("Sarah") # agrego un elemento
print(lista_grande)
lista_grande.insert(2,"Paul") # agrego un elemento en la posicion 2
print(lista_grande)
lista_grande.extend(["jorge",234.35,"Martha", "Judith"]) # extender una lista
print(lista_grande)
lista_grande.extend(lista_notas)
print(lista_grande)
print(lista_grande.index("Sarah")) # devuelve la posicion de ese string
print("Sarah" in lista_grande) # devuelve si esta o no... true or false
lista_grande.remove(234.35) # remueve un elemento
print(lista_grande)
lista_grande.pop() # elimina el ultimo
print(lista_grande)

listita = [23.5, "ariel", 12]
lista_sumanada = lista_nombres + lista_grande + listita
print(lista_sumanada)
listita = [23.5, "ariel", 12] *2
lista_sumanada = lista_nombres + lista_grande + listita
print(lista_sumanada)
print(len(lista_sumanada))     # cantidad de elementos de una lista