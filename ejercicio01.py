# Ejercicio 01
# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de
# una compra de productos de prevención de contagio, de cada una debe obtener los
# siguientes datos:
# · El tipo ("barbijo", "jabón" o "alcohol")
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de
# stock.

producto_ingresado = input("Por favor ingrese el tipo de producto (barbijo, jabon, alcohol): ")

while (not producto_ingresado == "barbijo" and not producto_ingresado == "jabon" and not producto_ingresado == "alcohol"):

    producto_ingresado = input("Por favor ingrese uno de los siguientes productos (barbijo, jabon, alcohol): ")

precio_ingresado = input("Por favor ingrese el precio: ")

while precio_ingresado.isalpha():

    precio_ingresado = input("Por favor ingrese un precio correcto: ")

cantidad_ingresado = input("Por favor ingrese la cantidad de unidades (1-100): ")

while cantidad_ingresado.isalpha():

    cantidad_ingresado = input("Por favor ingrese una cantidad de unidades correcta (1-100): ")

cantidad_ingresado = int(cantidad_ingresado)

while (cantidad_ingresado < 1 or cantidad_ingresado > 100):

    cantidad_ingresado = int(input("Por favor ingrese una cantidad de unidades correcta (1-100): "))

marca_ingresado = input("Por favor ingrese la marca del producto: ")

fabricante_ingresado = input("Por favor ingrese el fabricante del producto del producto: ")

# aca mostramos los datos ingresados

print(f"el producto ingresado fue {producto_ingresado}\ncantidad solicitada: {cantidad_ingresado} con un costo de $ {precio_ingresado} por unidad\nmarca: {marca_ingresado}\nfabricante: {fabricante_ingresado}")