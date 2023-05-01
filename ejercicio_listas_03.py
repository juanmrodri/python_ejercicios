# 3-
# Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
# de memoria es la que mas ocurrencias tiene dentro de esa lista.

numeros_ingresados = [1, 3, 5, 6, 3, 5, 0, 3, 1]

posicion_de_memoria_repetida = 0
numero_repetido = 0

# confirmacion = "s"

# while confirmacion == "s":

#     numero_ingresado = input("Por favor ingrese un numero: ")

#     while numero_ingresado.isalpha():
        
#         numero_ingresado = input("Por favor ingrese un numero valido: ")
    
#     numero_ingresado = int(numero_ingresado)

#     confirmacion = input("desea ingresar otro numero? (s/n)")
contador_repeticiones = 0

for numero in range(len(numeros_ingresados)):

    aux_num = numeros_ingresados[numero]
    print(f"{aux_num}")    
    for numero_dos in range(len(numeros_ingresados)):

        
        print(f"\t{numeros_ingresados[numero_dos]}")    
        if aux_num == numeros_ingresados[numero_dos]:

            contador_repeticiones = contador_repeticiones+1
            print(f"\t\t{contador_repeticiones}")
        



    
