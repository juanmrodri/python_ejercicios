# Ejercicio 07
# Tomando como base el ejercicio anterior:
# 1. Contar los pares.
# 2. Encontrar el mas grande de los impares.

numeros_ingresados = []
cantidad_pares = 0
impar_mayor = 0
impar_menor = 0
bandera_primer_impar = True

for numero in range(5):

    numero_ingresado = input("Por favor ingrese un numero entero: ")

    while numero_ingresado.isalpha():

        numero_ingresado = input("Por favor ingrese un NUMERO entero valido: ")
    
    numero_ingresado = int(numero_ingresado)

    numeros_ingresados.append(numero_ingresado)


for numero in range(len(numeros_ingresados)):
    
    if numeros_ingresados[numero] % 2 == 0:
        
        cantidad_pares = cantidad_pares+1
    elif not(numeros_ingresados[numero] % 2 == 0):
        
        if bandera_primer_impar == True:
            bandera_primer_impar = False
            impar_mayor = numeros_ingresados[numero]
            impar_menor = numeros_ingresados[numero]
        elif numeros_ingresados[numero] > impar_mayor:
            impar_mayor = numeros_ingresados[numero]
       


