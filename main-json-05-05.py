import json

lista = []

#lista.append({"id":1, "nombre":"Juan","apellido":"Rodriguez","edad":33})

file = open("personas.json", "r")

lista = json.load(file)

file.close()

for persona in lista:

    print(persona)