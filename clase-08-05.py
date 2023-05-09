

with open("DATA.csv","r") as file:

    contenido = file.read()


lista = []

lista_personas = []

lista = contenido.split("\n")

for persona in lista:
    p = persona.split(",")

    per_dict = {}

    per_dict['id'] = int(p[0])
    per_dict['nombre'] = p[1]
    per_dict['apellido'] = p[2]
    per_dict['email'] = p[3]
    per_dict['genero'] = p[4]
    per_dict['edad'] = int(p[5])
    lista_personas.append(per_dict)

for persona in lista_personas:

    print(persona)