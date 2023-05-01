# Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
# autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
# marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
# listas primero, y despues usando listas y comparar la composición del código.

seguir = "s"

while seguir == "s":

    # solo nombre
    marca_ingresada = input("Ingrese la marca del auto: ")

    # anio
    anio_ingresado = input("ingrese el anio del modelo: ")

    while anio_ingresado.isdigit() == False:

        anio_ingresado = input("Por favor ingrese un anio correcto ")
        if anio_ingresado.isdigit():
            anio_ingresado = int(anio_ingresado)

    print((marca_ingresada))
    print((anio_ingresado))

    seguir = input("Desea continuar s/n: ")

print("Fin del programa")
