#archivos

# archivo = open("prueba.txt", "r")

# #print(archivo.read())

# nuevo_archivo = archivo.readlines() # esto me devuelve una lista de strings

# # hay que intentar hacer lo menos posible con el archivo abierto
# archivo.close()

# print(nuevo_archivo)

# with open("prueba.txt", "r") as archivo:

#     contenido = archivo.readlines()

# for linea in contenido:

#     print(linea)

personas = []

with open("DATA.csv","r") as file:

    for linea in file:
        linea = linea.replace("\n","")
        linea = linea.split(",")
        personas.append(linea)
        print(linea)

for persona in personas:

    print(persona)