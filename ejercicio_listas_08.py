# Escribir un programa que le pida al usuario ingresar una lista de nombres de personas
# (previamente validada) y luego le pidan 1 solo nombre en específico. Se debe buscar
# el nombre especifico en la lista de nombres y si esta presente el programa deberá
# imprimir la posición del nombre en la lista, la posición de memoria donde se encuentra
# ese nombre y la cantidad de caracteres que tiene el nombre, si no se encuentra, se
# deberá informar por pantalla.

lista_personas = []

confirmacion = "s"
bandera_encontrado = False


while confirmacion == "s":

    nombre_ingresado = input("Por favor ingrese un nombre: ")

    while nombre_ingresado.isdigit():
        
        nombre_ingresado = input("Por favor ingrese un nombre valido: ")

    for nombre in range(len(lista_personas)):
     
        while nombre_ingresado == lista_personas[nombre]:
             
            nombre_ingresado = input(f"Por favor, intente con otro nombre, ese nombre ya esta ingresado, no se aceptan {nombre_ingresado}s: ")
             
    lista_personas.append(nombre_ingresado)

    confirmacion = input("desea ingresar otro nombre? (s/n)")

nombre_a_buscar = input("Por favor ingrese el nombre a buscar: ")

while nombre_a_buscar.isdigit():
        
        nombre_a_buscar = input("Por favor ingrese un nombre valido: ")

for nombre in range(len(lista_personas)):
     
    if nombre_a_buscar == lista_personas[nombre]:
          
            print(f"La posicion en la lista del nombre es: {nombre}\n"
                  f"La direccion de memoria es: {id(lista_personas[nombre])}\n"
                  f"La cantidad de caracteres que tiene el nombre es: {len(lista_personas[nombre])}")
            bandera_encontrado = True       

if bandera_encontrado == False:
        
    print("El nombre no existe en la lista!")
          


