# Realizar un programa que permita el ingreso de temperaturas a lo largo de una
# semana (Los 7 días de la semana, no necesariamente se ingresan en orden. Por
# ejemplo, puedo cargar primero el miércoles, luego el domingo, etc.). Dadas estas
# temperaturas debemos obtener distintas estadísticas.
# Para ello se deberán implementar distintas funciones:
# 1. Una que permita la carga de todas las temperaturas (día y temperatura).
# 2. Una que permita el pedido y validación de una temperatura. La misma
# retornará una temperatura válida.
# 3. Una que reciba como parámetro la lista y retorne el promedio de
# temperaturas.
# 4. Una que calcule la temperatura máxima.
# 5. Una que gestione un menú de usuario, el cual deberá tener las siguientes
# opciones:
# a. Cargar temperaturas
# b. Mostrar temperaturas (junto con sus días)
# c. Mostrar máxima temperatura con su día. (tener en cuenta que puede
# haber varios días con la misma temperatura)
# d. Mostrar promedio.
# e. Salir
# Nota: No se podrá entrar a las opciones b, c y d si no se cargaron los datos en la
# opción a.

def Cargar_Temperatura():

    aux_temperatura_ingresada = input("Por favor ingrese la temperatura (-90 y 50): ")

    while aux_temperatura_ingresada.isalpha():

        aux_temperatura_ingresada = input("Por favor debe ingresar una temperatura valida: ")
    
    aux_temperatura_ingresada = int(aux_temperatura_ingresada)

    while not(aux_temperatura_ingresada > -91 and aux_temperatura_ingresada < 51):

        aux_temperatura_ingresada = input("Por favor debe ingresar una temperatura valida (-90 y 50): ")

        while aux_temperatura_ingresada.isalpha():

            aux_temperatura_ingresada = input("Por favor debe ingresar una temperatura valida: ")

        aux_temperatura_ingresada = int(aux_temperatura_ingresada)

    return aux_temperatura_ingresada

def Carga_Dia_y_Temperatura():

    aux_datos_ingresados = {}

    aux_dia_ingresado = input("Por favor indique el dia en el que se cargara la temperatura (lunes, martes, miercoles, jueves, viernes, sabado, domingo): ")
    
    while (not aux_dia_ingresado == "lunes" and not aux_dia_ingresado == "martes" and not aux_dia_ingresado == "miercoles" and not aux_dia_ingresado == "jueves" and not aux_dia_ingresado == "viernes" and not aux_dia_ingresado == "sabado" and not aux_dia_ingresado == "domingo"):

        aux_dia_ingresado = input("Por favor indique un dia valido (lunes, martes, miercoles, jueves, viernes, sabado, domingo): ")

    temperatura_ingresada = Cargar_Temperatura()

    aux_datos_ingresados = {aux_dia_ingresado: temperatura_ingresada}

    #aux_datos_ingresados[aux_dia_ingresado]=[temperatura_ingresada]

    print(f"{aux_datos_ingresados}")

    return aux_datos_ingresados


    

    


#########################################################################################################
#aca terminan las funciones, despues hay que moverlas a otro archivo

respuesta = 0

semana = [] # aca guardamos el dic

dias_y_temperaturas = {}



while not(respuesta == "e"):

    print("a. Carga de temperaturas\n"
          "b. Mostrar temperaturas (junto con sus días)\n"
          "c. Mostrar máxima temperatura con su día.\n"
          "d. Mostrar promedio\n"
          "e. Salir\n")
    
    respuesta = input("Por favor ingrese una opcion: ")

    match respuesta:

        case "a":

            Carga_Dia_y_Temperatura()












