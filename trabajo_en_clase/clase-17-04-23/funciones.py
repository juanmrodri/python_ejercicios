
def sumar_f1():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    rta = a + b
    print("La suma es " + str(rta))

def sumar_f2():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    rta = a + b
    return rta

def sumar_f3(a, b):
    rta = a + b
    print("La suma es " + str(rta))

def sumar_f4(a, b):
    """suma dos enteros y retorna el resultado

    Args:
        a (int): primer numero a sumar
        b (int): segundo numero a sumar

    Returns:
        int: suma de los parametros ingresados
    """
    rta = a + b
    return rta