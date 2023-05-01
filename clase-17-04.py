# prueba de funcion, para ver como saca por referencia un valor una funcion o retorno
# si le pasamos por referencia a una funcion un tipo de dato inmutable (int, float, bool, str) la funcion, no lo puede modificar
# si tenemos una lista por ejemplo, que es un tipo de dato mutable, la funcion si modifica la variable

def duplicar(numero):
    print(f"2- Al comienzo de la funcion el numero vale {numero}")
    print(id(numero))
    numero = numero*2
    print(f"3- Al final de la funcion el numero vale {numero}")

    return numero

def agregar_cien(lista):

    lista.append("100")

##################################################################

numero = 20

lista = []

print(f"1- Al comienzo del programa el numero vale {numero}")

print(id(numero))

numero = duplicar(numero)

print(f"4- Al final del programa el numero vale {numero}")

print(lista)

print(id(lista))

agregar_cien(lista)

print(lista)

print(id(lista))