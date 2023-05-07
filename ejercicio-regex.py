import re

# texto = "Holis este es un texto de prueba. Es asi"

# ejemplos

# retorno = re.search("z", texto)

# if retorno:
    
#     print(retorno.group())

# else:
    
#     print("no existe")

# retorno = re.findall("xz", texto, re.IGNORECASE)

# if (not len(retorno) == 0): # findall crea una lista, si no encuentra alguna ocurrencia, crea una lista igual, pero vacia, entonces si queremos capturar eso, podemos usar el len
    
#         print(retorno)

# else:
     
#      print("No se encontraron ocurrencias")

tema ={
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
}

fecha_de_carga_ordenada = []

hora_de_carga_sin_segundos = []

# Tipo : BZRP MUSIC SESSIONS
# Artista: QUEVEDO
# Numero: 52
# Reproducciones: 227 M
# Duración: 204 segundos
# Codigo: A_g3lMcWVy0
# Fecha de carga:6/7/2022
# Hora de carga: 00:00

titulo = tema['title'].split("||")

artista = titulo[0].strip()

tipo = titulo[1].strip()

tipo = tipo.split(" #")

tipo = tipo[0]

tipo = tipo.upper()

numero = re.findall("#([^ ]*)",titulo[1])

numero = numero[0]

reproducciones = str(tema['views'])

reproducciones = re.findall("\d{3}", reproducciones)

reproducciones = reproducciones[0]

duracion = tema['length']

codigo = tema['url'].split("=")

codigo = codigo[1]

fecha_y_hora = tema['date'].split(" ")

fecha_de_carga = fecha_y_hora[0]

#fecha_de_carga = re.findall("\d" , fecha_de_carga)

fecha_de_carga = fecha_de_carga.split("-")

posicion = len(fecha_de_carga)-1

while posicion > -1:
    
    fecha_de_carga_ordenada.append(fecha_de_carga[posicion])

    posicion = posicion-1

fecha_de_carga_ordenada = "/".join(fecha_de_carga_ordenada)

hora_de_carga = fecha_y_hora[1]

hora_de_carga = hora_de_carga.split(":")

posicion = len(hora_de_carga)-2 #aca descartamos los segundos

while posicion > -1:

    hora_de_carga_sin_segundos.append(hora_de_carga[posicion])

    posicion = posicion-1

hora_de_carga_sin_segundos = ":".join(hora_de_carga_sin_segundos)


########### aca lo printeos ############

print(f"Tipo: {tipo}")
print(f"Artista: {artista}")
print(f"Numero: {numero}")
print(f"Reproducciones: {reproducciones} M")
print(f"Duracion: {duracion} segundos")
print(f"Codigo: {codigo}")
print(f"Fecha de carga: {fecha_de_carga_ordenada}")
print(f"Hora de carga: {hora_de_carga_sin_segundos}")


