# Pedir al usuario que ingrese 5 números (verificar que sea un número, comprendidoentre -1000 y 1000).
# Mostrar:
# 1. Todos los números ingresados.
# 2. Suma de los positivos.
# 3. Producto de los negativos.
# 4. Promedio de todos los números.

suma_positivos = 0
producto_negativos = 1
bandera_negativos_ingresados = True
promedio_numeros = 0
TAM = 5 # cantidad de vueltas
primer_numero_ingresado = None
segundo_numero_ingresado = None
tercer_numero_ingresado = None
cuarto_numero_ingresado = None
quinto_numero_ingresado = None

for i in range(TAM):

    numero_ingresado = input("Ingrese un numero: ")

    while numero_ingresado.isalpha():

        numero_ingresado = input("Por favor ingrese un numero: ")
    
    numero_ingresado = int(numero_ingresado)

    while not(numero_ingresado > -1000 and numero_ingresado < 1000):

        numero_ingresado = input("Por favor ingrese un numero comprendido entre -1000 y 1000: ")

        while numero_ingresado.isalpha():

            numero_ingresado = input("Por favor ingrese un numero: ")

        numero_ingresado = int(numero_ingresado)  

    if numero_ingresado > -1:
        suma_positivos = suma_positivos + numero_ingresado
    else:
        bandera_negativos_ingresados = False
        producto_negativos = producto_negativos * numero_ingresado

    promedio_numeros = promedio_numeros + numero_ingresado

    # para printear afuera del loop
    match i:

        case 0:
            primer_numero_ingresado = numero_ingresado
        case 1:
            segundo_numero_ingresado = numero_ingresado
        case 2:
            tercer_numero_ingresado = numero_ingresado
        case 3:
            cuarto_numero_ingresado = numero_ingresado
        case 4:
            quinto_numero_ingresado = numero_ingresado

promedio_numeros = promedio_numeros / TAM

if bandera_negativos_ingresados == True:
    producto_negativos = 0

print("Los numeros ingresados fueron\n"
      "- ",primer_numero_ingresado,"\n"
      "- ",segundo_numero_ingresado,"\n"
      "- ",tercer_numero_ingresado,"\n"
      "- ",cuarto_numero_ingresado,"\n"
      "- ",quinto_numero_ingresado,"\n")

print("La suma de los numeros positivos es:", + suma_positivos)
print("El producto de los negativos es:", + producto_negativos)
print("El promedio de los numeros es:", + promedio_numeros)
