# Ejercicio 05
# Pedir al usuario que ingrese 5 números enteros, mostrar los valores ingresados y
# calcular la suma de los mismos.
# ahora con lista

numeros_ingresados = []
suma_total = 0

for numero in range(5):

    numero_ingresado = input("Por favor ingrese un numero entero: ")

    while numero_ingresado.isalpha():

        numero_ingresado = input("Por favor ingrese un NUMERO entero valido: ")
    
    numero_ingresado = int(numero_ingresado)

    numeros_ingresados.append(numero_ingresado)


for numero in range(len(numeros_ingresados)):
    
    print(f"{numeros_ingresados[numero]}")

for numero in range(len(numeros_ingresados)):
    
    suma_total = suma_total + numeros_ingresados[numero] 
