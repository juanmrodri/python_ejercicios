#Es la gala final de Gran Hermano y la producción nos pide un programa para contar
#los votos de los televidentes y saber cuál será el participante que ganará el juego.
#Los participantes finalistas son: Nacho, Julieta y Marcos.
#El televidente debe ingresar:

#● Nombre del votante
#● Edad del votante (debe ser mayor a 13)
#● Género del votante (masculino, femenino, otro)
#● El nombre del participante a quien le dará el voto positivo.

#No se sabe cuántos votos entrarán durante la gala.
#Se debe informar al usuario:

#A. El promedio de edad de las votantes de género femenino
#B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.
#C. Nombre del votante más joven que votó a Nacho.
#D. Nombre de cada participante y porcentaje de los votos qué recibió.
#E. El nombre del participante que ganó el reality (El que tiene más votos)

import os

confirmacion = "s"
votante_femenino_ingresado = 0
votante_femenino_edad = 0
votante_genero_masculino = 0
promedio_edad_votante_femenino = 1
bandera_votante_femenino = True
bandera_votante_mas_joven_nacho = True
nombre_votante_mas_joven_nacho_minimo = None
cantidad_votos_nacho = 0
cantidad_votos_julieta = 0
cantidad_votos_marcos = 0
porcentaje_votos_nacho = 0
porcentaje_votos_julieta = 0
porcentaje_votos_marcos = 0
participante_ganador = None

print("Bienvenido!\n")

while confirmacion == "s":

    # pedido de nombre
    nombre_ingresado = input("Por favor ingrese su nombre: ")

    while nombre_ingresado.isdigit():
        
        nombre_ingresado = input("Por favor ingrese su nombre valido: ")

    # pedido de edad
    edad_ingresada = input("Por favor ingrese su edad(+13): ")

    while edad_ingresada.isalpha():

        edad_ingresada = input("Por favor debe ingresar una edad valida: ")
    
    edad_ingresada = int(edad_ingresada)

    while not(edad_ingresada > 13 and edad_ingresada < 100):

        edad_ingresada = input("Usted debe ser mayor de 13 anios para votar, indique a otra persona mayor para que vote por usted: ")

        while edad_ingresada.isalpha():

            edad_ingresada = input("Por favor debe ingresar una edad valida: ")

        edad_ingresada = int(edad_ingresada)

    # pedido de genero
    genero_ingresado = input("Por favor indique su genero (m, f, nb): ")
    
    while (not genero_ingresado == "m" and not genero_ingresado == "f" and not genero_ingresado == "nb"):

        genero_ingresado = input("Por favor ingrese un genero valido (m, f, nb): ")
    
    # pedido de voto
    voto_ingresado = input("Por favor indique a quien quiere votar (Nacho, Julieta, Marcos): ")

    while (not voto_ingresado == "Nacho" and not voto_ingresado == "Julieta" and not voto_ingresado == "Marcos"):

        voto_ingresado = input("Por favor seleccione uno de estos participantes (Nacho, Julieta, Marcos): ")
    
    # posterior a pedido de datos

    if genero_ingresado == "f":

        bandera_votante_femenino = False
        votante_femenino_ingresado = votante_femenino_ingresado+1
        votante_femenino_edad = votante_femenino_edad + edad_ingresada

    elif genero_ingresado == "m":

        if (edad_ingresada > 24 and edad_ingresada < 41) and (voto_ingresado == "Nacho" or voto_ingresado == "Julieta"):

            votante_genero_masculino = votante_genero_masculino+1

    if voto_ingresado == "Nacho":

        if bandera_votante_mas_joven_nacho == True:

            bandera_votante_mas_joven_nacho = False
            votante_mas_joven_nacho_minimo = edad_ingresada
            votante_mas_joven_nacho_maximo = edad_ingresada
            nombre_votante_mas_joven_nacho_minimo = nombre_ingresado

        elif edad_ingresada < votante_mas_joven_nacho_minimo:
            votante_mas_joven_nacho_minimo = edad_ingresada
            nombre_votante_mas_joven_nacho_minimo = nombre_ingresado

        else:
            edad_ingresada == votante_mas_joven_nacho_minimo
            nombre_votante_mas_joven_nacho_minimo = "Existe mas de un votante"

    match voto_ingresado:

        case "Nacho":
            cantidad_votos_nacho = cantidad_votos_nacho+1
        
        case "Julieta":
            cantidad_votos_julieta = cantidad_votos_julieta+1
        
        case "Marcos":
            cantidad_votos_marcos = cantidad_votos_marcos+1
    
    cantidad_total_votos = cantidad_votos_nacho + cantidad_votos_julieta + cantidad_votos_marcos

    confirmacion = input("Desea ingresar otro voto? ")

os.system("cls")

#calculos fuera del bucle

if bandera_votante_femenino == False:

    promedio_edad_votante_femenino = votante_femenino_edad / votante_femenino_ingresado

else:
    # asi mostramos un 0, ya que no hay datos generados
    promedio_edad_votante_femenino = 0

porcentaje_votos_nacho = (cantidad_votos_nacho * 100) / cantidad_total_votos
porcentaje_votos_julieta = (cantidad_votos_julieta * 100) / cantidad_total_votos
porcentaje_votos_marcos = (cantidad_votos_marcos * 100) / cantidad_total_votos

if porcentaje_votos_nacho > porcentaje_votos_julieta and porcentaje_votos_nacho > porcentaje_votos_marcos:
    participante_ganador = "Nacho"
elif porcentaje_votos_julieta > porcentaje_votos_nacho and porcentaje_votos_julieta > porcentaje_votos_marcos:
    participante_ganador = "Julieta"
elif porcentaje_votos_nacho == porcentaje_votos_julieta:
    participante_ganador = "Existe un empate"
elif porcentaje_votos_nacho == porcentaje_votos_marcos:
    participante_ganador = "Existe un empate"
elif porcentaje_votos_julieta == porcentaje_votos_marcos:
    participante_ganador = "Existe un empate"
else:
    participante_ganador = "Marcos"


print(f"A. Promedio de edad de las votantes de género femenino: {promedio_edad_votante_femenino}")
print(f"B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta: {votante_genero_masculino}")
print(f"C. Nombre del votante más joven que votó a Nacho: {nombre_votante_mas_joven_nacho_minimo}")
print(f"D. Votos Nacho: {porcentaje_votos_nacho:.2f}%\n"
      f"D. Votos Julieta: {porcentaje_votos_julieta:.2f}%\n"
      f"D. Votos Marcos: {porcentaje_votos_marcos:.2f}%")
print(f"E. El nombre del participante que ganó el reality: {participante_ganador}")