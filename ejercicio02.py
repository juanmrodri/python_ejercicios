# Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
# python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
# al ingresar el número debemos mostrarle que regla de estilo representa y su
# descripción (Sacar la información de las diapositivas de las reglas de estilo).
# En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario “Error,
# regla de estilo inexistente”

import os

while True:

    respuesta_ingresada = input(
    "Bienvenido, seleccione una opcion para ver la regla de estilo:\n\n"
    "1) Cual es el sentido?\n"
    "2) Que es PEP?\n"
    "3) Que es PEP8?\n"
    "4) Indentado\n"
    "5) Tamanio maximo de linea\n"
    "6) Lineas en blanco\n"
    "7) Comentarios\n"
    "8) Nombres\n")

    print("\n")

    match respuesta_ingresada:
        case "1":
            print("Según Guido van Rossum, el código es leído más\n"
                  "veces que escrito, por lo que resulta importante\n"
                  "escribir código que no sólo funcione, sino que\n"
                  "además pueda ser leído con facilidad.\n")
            
        case "2":
            print("Python Enhancement Proposal es un documento\n"
                  "que proporciona información a la comunidad de\n"
                  "Python, o que describe una nueva característica.\n")

        case "3":
            print("Es un conjunto de recomendaciones cuyo objetivo\n"
                  "es ayudar a escribir código más legible y abarca\n"
                  "desde cómo nombrar variables, al número máximo\n"
                  "de caracteres que una línea debe tener.\n")

        case "4":
            print("Python no usa {} para designar bloques de código\n"
                  "como otros lenguajes de programación, sino que\n"
                  "usa bloques identados para indicar que un\n"
                  "determinado bloque de código pertenece a por\n"
                  "ejemplo un if.\n")

        case "5":
            print("Se recomienda limitar el tamaño de cada línea a\n"
                  "79 caracteres, para evitar tener que hacer scroll a\n"
                  "la derecha.\n")

        case "6":
            print("El uso de espacios en blanco mejora la legibilidad\n"
                  "del código, y es por lo que la PEP8 indica dónde\n"
                  "debemos usar espacios y dónde no.\n")

        case "7":
            print("Cualquier comentario que contradiga el código es\n"
                  "peor que ningún comentario.Si actualizamos el\n"
                  "código, se debe actualizar loscomentarios para\n"
                  "evitar crear inconsistencias. Evitar comentarios\n"
                  "poco descriptivos que no aporten nada más allá\n"
                  "de lo que ya se ve a simple vista.\n")
        
        case "8":
            print("Funciones: Uso de snake_case, letras en\n"
                  "minúscula separadas por guión bajo: mi_funcion.\n"
                  "Variables: Al igual que las funciones: variable,\n"
                  "mi_variable.\n"
                  "Clases: Uso de CamelCase, usando mayúscula y\n"
                  "sin barra baja: MiClase, ClaseDePrueba.\n")

        case _:
            print("Disculpe la opcion ingresada no existe, vuelva a intentar\n")

    os.system("pause")


