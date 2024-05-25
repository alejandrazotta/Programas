mitupla =("Alemania","Francia","España","Italia","Brasil")
mi_diccionario ={mitupla[0]:"Berlin",mitupla[1]:"Paris",mitupla[2]:"Madrid",mitupla[3]:"Roma",mitupla[4]:"Brasilia"}
print(mi_diccionario)
print(mi_diccionario["Brasil"])

# Integrar una tupla a un diccionario

mi_diccionario2={23:"Jordan",\
                 "Nombre":"Michel",\
                 "Equipo": "Chigago",\
                 "Medallas": (1191,1992.1996,1998)}
print(mi_diccionario2)

mi_diccionario2={23:"Jordan",\
                 "Nombre":"Michel",\
                 "Equipo": "Chigago",\
                 "Anillos":{"Medallas": (1191,1992.1996,1998)}}
print(mi_diccionario2)

print(mi_diccionario2.keys())
print(mi_diccionario2.values())

print(len(mi_diccionario2))

# Integrar dos diccionarios

dicc1 = {23:"Jordan","Equipo":"Chicago"}
dicc2 = {8:"El Chavo", 100:"The houndred"}
print(dicc1)
print(dicc2)
dicc1.update(dicc2) #concatena dicc1 y dicc2 y lo pone en dicc1
print(dicc1)