
import re

def menu_opciones()->str:

    """menu de opciones para superheroes

    Returns:
        str: opcion seleccionada
    """

    respuesta = 0

    print("\t\t\t*** Bienvenido ***\n" 
          "A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n"
          "B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n"
          "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
          "D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
          "E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M\n"
          "F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F\n"
          "G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M\n"
          "H. Recorrer la lista y determinar la altura promedio de los superhéroes degénero F\n"
          "I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)\n"
          "J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
          "K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
          "L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).\n"
          "M. Listar todos los superhéroes agrupados por color de ojos.\n"
          "N. Listar todos los superhéroes agrupados por color de pelo.\n"
          "O. Listar todos los superhéroes agrupados por tipo de inteligencia\n"
          "P. Salir\n")
    
    respuesta = input("Por favor ingrese una opcion: ")

    while respuesta.isdigit():

        respuesta = input("Por favor ingrese una opcion opcion valida!: ")

    respuesta = respuesta.capitalize()

    return respuesta

def stark_normalizar_datos(lista: list):

    """Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)

    Returns:
        _type_: retorna un 1 si tuvo exito, 0 si la lista esta vacia o -1 si no existian datos en la lista para normalizar
    """

    ret = 0

    verificacion_de_modificacion = (verificar_modificacion(lista))

    modificacion_realizada = False
 
    if (not len(lista)==0) and verificacion_de_modificacion:

        print(f"esto devuelve verificacion: {verificacion_de_modificacion}")

        for personaje in lista:

            for item in personaje:

                if not type(personaje[item]) == int and not type(personaje[item]) == float:

                    valor = re.search("\d", personaje[item])

                    if valor:

                        valor_aux = re.search("\.", personaje[item])

                        if valor_aux:

                            modificacion_realizada = True
                            personaje[item] = float(personaje[item])

                            #print(type(personaje[item]))

                        else:

                            modificacion_realizada = True
                            personaje[item] = int(personaje[item])

                            #print(type(personaje[item]))     

        if modificacion_realizada:

            ret = 1

            print("Modificacion realizada")
            
        else:

            ret = -1

    else:
        
        print("Error: Lista de héroes vacía")
    
    return ret

def verificar_modificacion(lista: list)->int:


    """verifica si es necesario normalizar algun valor, si por lo menos existe uno, retorna

    Returns:
        _type_: 0 si no existe ningun valor a modificar o un numero distinto a 0 para indicar que si es necesario
    """
    evaluar = 0

    if (not len(lista)==0):

        for personaje in lista:

            for item in personaje:

                if (not type(personaje[item]) == int) and (not type(personaje[item]) == float):

                    evaluar = evaluar+1
                    break

    return evaluar

# funcion de prueba para usar obtener nombre, ya que estan en mayuscula todos

def nombres_a_lower(superheroe:dict):


    for key in superheroe:

        if key == "nombre":

           superheroe[key] =  superheroe[key].lower()


def modificar_nombre_a_mayuscula(superheroe:dict):

    for key in superheroe:

        if key == "nombre":

            hay_espacios = re.search(" ",superheroe[key])

            print(bool(hay_espacios))

            if (hay_espacios):

                hay_espacios = superheroe[key].split(" ")

                cantidad_palabras = len(hay_espacios)

                print(cantidad_palabras)

                for posicion in range(cantidad_palabras):

                    hay_espacios[posicion] = hay_espacios[posicion].replace(hay_espacios[posicion],hay_espacios[posicion].capitalize())

                    print(hay_espacios[posicion])
   
                print(hay_espacios)
                
                unir_espacios = " ".join(hay_espacios)

                print(unir_espacios)

                superheroe[key] = superheroe[key].replace(superheroe[key],unir_espacios)

                print(superheroe[key])

            elif hay_espacios == None:

                hay_espacios = re.search("-",superheroe[key])

                if (not hay_espacios == None):

                    hay_espacios = superheroe[key].split("-")

                    cantidad_palabras = len(hay_espacios)

                    print(cantidad_palabras)

                    for posicion in range(cantidad_palabras):

                        hay_espacios[posicion] = hay_espacios[posicion].replace(hay_espacios[posicion],hay_espacios[posicion].capitalize())

                        print(hay_espacios[posicion])
    
                        print(hay_espacios)
                
                    unir_espacios = "-".join(hay_espacios)

                    print(unir_espacios)

                    superheroe[key] = superheroe[key].replace(superheroe[key],unir_espacios)

                    print(superheroe[key])

            else:

                superheroe[key] = superheroe[key].replace(superheroe[key],superheroe[key].capitalize())



            #print(superheroe[key])

                #print(f"\t{letra}")


    #print(f"{superheroe['nombre']:>20} - {superheroe['identidad']:<30} {superheroe['empresa']:<15} {superheroe['altura']:10.2f} {superheroe['peso']:10.2f} {superheroe['genero']:<3} {superheroe['color_ojos']:>30} {superheroe['color_pelo']:<20} {superheroe['fuerza']:>5} {superheroe['inteligencia']}")

def buscar_espacio_o_guin(cadena: str)-> str:

    pass

def obterner_nombre(superheroe: dict):

    ret_nombre = None

    for key in superheroe:

        if key == "nombre":

            hay_espacios = re.search(" ",superheroe[key])

            if (hay_espacios):

                hay_espacios = superheroe[key].split(" ")

                cantidad_palabras = len(hay_espacios)

                for posicion in range(cantidad_palabras):

                    hay_espacios[posicion] = hay_espacios[posicion].replace(hay_espacios[posicion],hay_espacios[posicion].capitalize())
                
                ret_nombre = " ".join(hay_espacios)

            elif hay_espacios == None:

                hay_guiones = re.search("-",superheroe[key])

                if (not hay_guiones == None):

                    hay_guiones = superheroe[key].split("-")

                    cantidad_palabras = len(hay_guiones)

                    for posicion in range(cantidad_palabras):

                        hay_guiones[posicion] = hay_guiones[posicion].replace(hay_guiones[posicion],hay_guiones[posicion].capitalize())
                
                    ret_nombre = "-".join(hay_guiones)

                else:

                 ret_nombre = superheroe[key].replace(superheroe[key],superheroe[key].capitalize())

            

    return ret_nombre

def cargar_lista(lista_personajes: list, lista_destino: list)-> None:

    """Carga una lista con los datos recibidos 

    Args:
        lista_personajes (list): lista origen
        lista_destino (list): lista destino
    """

    if (type(lista_personajes)==list and type(lista_destino)==list):

        for heroe in lista_personajes:
            lista_destino.append(heroe.copy()) # creamos una copia de las posiones de la lista original, ya que sino, tendriamos 2 direcciones de memoria que apuntan a los mismos valores

        print("Lista cargada correctamente!")

    else:
        print("Existe algun problema con el tipo de datos, por favor intentar luego")


def mostrar_un_superheroe(superheroe: dict)-> None:

    """Muestra un solo superheroe
    """

    #auxiliar_altura = float(superheroe['altura'])
    #auxiliar_peso = float(superheroe['peso'])

    print(f"{superheroe['nombre']:>20} - {superheroe['identidad']:<30} {superheroe['empresa']:<15} {superheroe['altura']:10.2f} {superheroe['peso']:10.2f} {superheroe['genero']:<3} {superheroe['color_ojos']:>30} {superheroe['color_pelo']:<20} {superheroe['fuerza']:>5} {superheroe['inteligencia']}")


def listar_superheroes(lista: list, mensaje:str)-> None:

    """Imprime un encabezado y llama, adentro de un for, a la funcion que imprime un solo superheroe
    """

    print(f"{mensaje}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("              nombre   identidad                         empresa          altura       peso genero               color de ojos color de pelo       fuerza inteligencia")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    for superheroe in lista:

        mostrar_un_superheroe(superheroe)

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



def imprimir_genero(lista: list, genero:str)->None:

    """Imprime un encabezado y llama, adentro de un for, a la funcion que imprime la lista filtrada por el genero en parametro
    """

    genero = genero.capitalize() # por si llega a venir una minuscula, igual esta hardcodeado aca

    print(" *** Lista de superheroes masculinos ***")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("              nombre   identidad                         empresa          altura       peso genero               color de ojos color de pelo       fuerza inteligencia")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for superheroe in lista:
        
        if superheroe['genero'] == genero:

            mostrar_un_superheroe(superheroe)
            
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def buscar_altura(lista: list, genero:str, valor_a_buscar:str)->dict:

    """Busca tanto maximos como minimos, dependiendo la opcion que ingresa en valor a buscar

    Returns:
        _type_: devuelve un diccionario con la posicion encontrada
    """

    bandera_primer_altura = True
    aux_mas_alto_posicion = {}
    aux_mas_bajo_posicion = {}
    aux_posicion_final = {}
    altura_contador = 0

    genero = genero.capitalize() # por si llega a venir una minuscula, igual esta hardcodeado aca

    # si se busca mayor hace esto

    for superheroe in lista:
    
        if superheroe['genero'] == genero:
            
            if bandera_primer_altura == True:

                bandera_primer_altura = False
                
                aux_altura_max = float(superheroe['altura'])

                aux_altura_min = float(superheroe['altura'])

                aux_mas_alto_posicion = superheroe

                aux_mas_bajo_posicion = superheroe

                aux_posicion_final = superheroe

            elif superheroe['altura'] > aux_altura_max:
                
                aux_altura_max = superheroe['altura']

                aux_mas_alto_posicion = superheroe
            
            elif superheroe['altura'] < aux_altura_min:
                
                aux_altura_min = superheroe['altura']
                
                aux_mas_bajo_posicion = superheroe
                
            if valor_a_buscar == "mayor":

                aux_posicion_final = aux_mas_alto_posicion

            elif valor_a_buscar == "menor":

                aux_posicion_final = aux_mas_bajo_posicion

    # aca chequeamos la posibilidad de alguna igualdad de valores, si el contador da mas de 

    altura_contador = buscar_igualdad_de_valores(lista,valor_a_buscar,aux_altura_max,aux_altura_min)

        
    print(altura_contador)

    return aux_posicion_final


def buscar_igualdad_de_valores(lista:list, valor_a_buscar:str,altura_max,altura_min)->int:

    """Recorre una lista buscando la igualdad de un valor, para contarlo

    Returns:
        _type_: retorna la cuenta
    """
    contador = 0

    for heroe in lista:

        if valor_a_buscar == "mayor":

            if heroe['altura'] == altura_max:

                contador = contador +1

        elif valor_a_buscar == "menor":

                if heroe['altura'] == altura_min:

                    contador = contador +1

    return contador

def agregar_altura_a_lista(diccionario, lista:list):

    """Agrega un diccionaro a la lista
    """
    lista.append(diccionario)


def convertir_campos_a_float(lista: list):

    """Convierte los campos con str a float para poder operar con los valores
    """

    for superheroe in lista:
        
        superheroe['altura'] = float(superheroe['altura'])
        superheroe['peso'] = float(superheroe['peso'])

def calcular_promedio(cantidad: int, total_acumulado):

    """Calcula el promedio

    Returns:
        _type_: retorna el promedio calculado
    """

    if (type(cantidad)==int):

        promedio = total_acumulado / cantidad

    return promedio

def calcular_altura_promedio(lista:list, genero:str)->float:

    """Calcula el promedio de alturas

    Returns:
        _type_: _description_
    """
    
    cantidad_superheroes = 0
    acumulador_alturas = 0
    promedio_calculado = 0

    genero = genero.capitalize() # por si llega a venir una minuscula, igual esta hardcodeado aca

    for superheroe in lista:

        if superheroe['genero'] == genero:

            cantidad_superheroes = cantidad_superheroes+1
            acumulador_alturas = acumulador_alturas + superheroe['altura']

    promedio_calculado = calcular_promedio(cantidad_superheroes,acumulador_alturas)

    return promedio_calculado

def mostrar_promedio(promedio:float, mensaje:str)->None:

    """Muestra un promedio en consola
    """

    print(f"{mensaje}{promedio:.2f}")


def agregar_todos_los_valores_a_lista(lista:list, lista_valores_extraidos:list, key_a_extraer:str)->None:

    for heroe in lista:

        lista_valores_extraidos.append(heroe[key_a_extraer])

def encontrar_valor_repetido_en_lista(lista:list, item:str)->bool:

    res = False

    for color in lista:

        if color == item:
            
            res = True

            break

    return res

def agregar_valores_filtrando(lista_filtrados:list, valores_sin_filtrar: list)->None:

    """Recibe una lista, donde se guardaran los datos filtrados, y otra lista con los valores repetidos a filtrar
    """
    for item in valores_sin_filtrar:

        if( not encontrar_valor_repetido_en_lista(lista_filtrados, item)):

            lista_filtrados.append(item)

def mostrar_heroes_filtrando_por_algun_valor(lista_filtrados:list, heroes: list, key_a_extraer:str)->None:

    """Filtra el listado a imprimir por algun key value determinado en key_a_extraer
    """
    for item in lista_filtrados:

        # si no tiene inteligencia
        if key_a_extraer == "inteligencia" and item == "":

            print("Does not have")

        print(item)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("              nombre   identidad                         empresa          altura       peso genero               color de ojos color de pelo       fuerza inteligencia")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for heroe in heroes:

            if (heroe[key_a_extraer] == item):
        
                mostrar_un_superheroe(heroe)
                
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


            


