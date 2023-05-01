#La real academia española nos pide desarrollar un pequeño programa que contenta el
#diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
#algoritmo que nos permita el ingreso de una palabra en español y su traducción al
#ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
#palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
#esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
#debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
#inglés. Recordar validar los datos de forma correcta.


respuesta_continuar = "s"
palabras_espaniol = []
palabras_ingles = []


while respuesta_continuar =="s":

    palabra_espaniol_ingresada = input("Por favor ingrese la palabra en espaniol: ")

    while palabra_espaniol_ingresada.isdigit():
        
        palabra_espaniol_ingresada = input("Por favor ingrese una palabra valida: ")

    for palabra in range(len(palabras_espaniol)):
        while palabra_espaniol_ingresada == palabras_espaniol[palabra]:
            palabra_espaniol_ingresada = input("Por favor ingrese una palabra que no exista en la lista: ")     
    
    palabras_espaniol.append(palabra_espaniol_ingresada)

    palabra_ingles_ingresada = input("Por favor ingrese la palabra en ingles: ")

    while palabra_ingles_ingresada.isdigit():
        
        palabra_ingles_ingresada = input("Por favor ingrese una palabra valida: ")
    
    palabras_ingles.append(palabra_ingles_ingresada)


    respuesta_continuar = input("Desea continuar (s/n): ")


for palabra in range(len(palabras_espaniol)):
    print(f"Espaniol: {palabras_espaniol[palabra]} Ingles: {palabras_ingles[palabra]}\n-------------------------------")
