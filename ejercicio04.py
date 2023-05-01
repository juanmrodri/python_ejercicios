#La división de alimentos está trabajando en un pequeño software para cargar las
#compras de ingredientes para la cocina de Industrias Wayne.
#Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
#para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
#de ingredientes.
#Se registra por cada compra:
#1. PESO: (entre 10 y 100 kilos)
#2. PRECIO POR KILO: (mayor a 0 [cero]).
#3. TIPO VARIEDAD: (vegetal, animal, mezcla).
#Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
#descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
#de descuento sobre el precio bruto.
#Se desea saber:
#A. El importe total a pagar, BRUTO sin descuento.
#B. El importe total a pagar con descuento (Solo si corresponde).
#C. Informar el tipo de alimento más caro.
#D. El promedio de precio por kilo en total.


TAM = 3 # total de vueltas
peso_ingresado_acumulado = 0
precio_ingresado_acumulado = 0
precio_total = 0
precio_con_descuento = 0
descuento_a_aplicar = 0
precio_alimento_mas_caro = 0
precio_alimento_mas_barato = 0
tipo_alimento_mas_caro = None
bandera_primer_alimento = True
cantidad_productos_ingresada = 0
promedio_precio_por_kilo = 0

while TAM > 0:

    # pedido de peso
    peso_ingresado = input("Por favor ingrese el peso (10 - 100 Kg): ")

    while peso_ingresado.isalpha():

        peso_ingresado = input("Por favor debe ingresar un peso valido (10 - 100 Kg): ")
    
    peso_ingresado = int(peso_ingresado)

    while not(peso_ingresado > 10 and peso_ingresado < 100):

        peso_ingresado = input("Por favor debe ingresar un peso valido entre 10 y 100 Kg: ")

        while peso_ingresado.isalpha():

            peso_ingresado = input("Por favor debe ingresar un peso valido: ")

        peso_ingresado = int(peso_ingresado)
    
    # pedido de precio por kilo
    precio_ingresado = input("Por favor ingrese el precio por kilo: ")

    while precio_ingresado.isalpha():

        precio_ingresado = input("Por favor debe ingresar un precio valido: ")
    
    precio_ingresado = int(precio_ingresado)

    while not(precio_ingresado > 0):

        precio_ingresado = input("Por favor debe ingresar un precio valido: ")

        while precio_ingresado.isalpha():

            precio_ingresado = input("Por favor debe ingresar un precio valido: ")

        precio_ingresado = int(precio_ingresado)

    # pedido de variedad (vegetal, animal, mezcla)
    varieda_ingresada = input("Por favor indique la variedad del producto (v, a, m): ")
    
    while (not varieda_ingresada == "v" and not varieda_ingresada == "a" and not varieda_ingresada == "m"):

        varieda_ingresada = input("Por favor ingrese la variedad valida (v, a, m): ")

    if bandera_primer_alimento == True:
        bandera_primer_alimento = False
        precio_alimento_mas_caro = precio_ingresado
        precio_alimento_mas_barato = precio_ingresado
        tipo_alimento_mas_caro = varieda_ingresada
    elif precio_ingresado > precio_alimento_mas_caro:
        precio_alimento_mas_caro = precio_ingresado
        tipo_alimento_mas_caro = varieda_ingresada

    peso_ingresado_acumulado = peso_ingresado_acumulado + peso_ingresado
    precio_ingresado_acumulado = precio_ingresado_acumulado + precio_ingresado

    cantidad_productos_ingresada = cantidad_productos_ingresada+1
    
    TAM = TAM -1

# calculos fuera del loop

precio_total = precio_ingresado_acumulado * peso_ingresado_acumulado

promedio_precio_por_kilo = precio_ingresado_acumulado / cantidad_productos_ingresada

if peso_ingresado_acumulado > 100:
    descuento_a_aplicar = 15.0
    precio_con_descuento = (precio_total * descuento_a_aplicar) / 100
    precio_con_descuento = precio_total - precio_con_descuento
elif precio_ingresado_acumulado > 300:
    descuento_a_aplicar = 25.0
    precio_con_descuento = (precio_total * descuento_a_aplicar) / 100

print(f"El importe Bruto es {precio_total:.1f}")
if precio_con_descuento > 0:
    print(f"El descuento es del {descuento_a_aplicar:.1f}")
    print(f"El importe con descuento es es {precio_con_descuento:.1f}")
else:
    print("No se aplica descuento al importe total")
print(f"El tipo de alimento mas caro es {tipo_alimento_mas_caro}")
print(f"El promedio de precio por kilo es {promedio_precio_por_kilo:.1f}")