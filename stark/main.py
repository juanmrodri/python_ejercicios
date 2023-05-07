from data_stark import lista_personajes
from funciones import *

# devolucion de la parte uno
# Part 1: imprimir_genero hace lo mismo en el if que el elif (:o) ---> ok
# en la funcion de la maxima altura: para que pasar el genero si despues preguntas por un literal? ---> ok
# La funcion es poco reutilizable y extensa Hay mucha repeticion de codigo. 
# Ojo. Para una primera enmtrega esta bien, pero tene en cuenta los contenidos que estamos viendo en estas ultimas 
# clases sobre funciones, reutilizacion.

lista_superheroes = []

lista_alturas_obtenidas = []

lista_colores_ojos = []

lista_colores_ojos_filtrados = []

lista_colores_pelo = []

lista_colores_pelo_filtrados = []

lista_tipo_inteligencia = []

lista_tipo_inteligencia_filtrados = [] 

respuesta_seleccionada = None

# for heroe in lista_personajes:
#     lista_superheroes.append(heroe.copy())

# for heroe in lista_superheroes:
#     colores.append[heroe['color_ojos']]

# menu

cargar_lista(lista_personajes, lista_superheroes)

while not(respuesta_seleccionada == "P"):

    # aca llamamos al menu
    match (menu_opciones()):

        # case "3":
        #     listar_superheroes(lista_superheroes)

        case "A":
            imprimir_genero(lista_superheroes, "M")

        case "B":
            imprimir_genero(lista_superheroes, "F")

        case "C":
            convertir_campos_a_float(lista_superheroes)
            aux_posicion_obtenida = buscar_altura(lista_superheroes,"M", "mayor")
            agregar_altura_a_lista(aux_posicion_obtenida, lista_alturas_obtenidas)
            print("Calculo realizado y guardado con exito")    

        case "D":
            convertir_campos_a_float(lista_superheroes)
            aux_posicion_obtenida = buscar_altura(lista_superheroes,"F", "menor")
            agregar_altura_a_lista(aux_posicion_obtenida, lista_alturas_obtenidas)
            print("Calculo realizado y guardado con exito")

        case "E":
            convertir_campos_a_float(lista_superheroes)
            aux_posicion_obtenida = buscar_altura(lista_superheroes,"M", "mayor")
            agregar_altura_a_lista(aux_posicion_obtenida, lista_alturas_obtenidas)
            print("Calculo realizado y guardado con exito")

        case "F":
            convertir_campos_a_float(lista_superheroes)
            aux_posicion_obtenida = buscar_altura(lista_superheroes,"F", "menor")
            agregar_altura_a_lista(aux_posicion_obtenida, lista_alturas_obtenidas)
            print("Calculo realizado y guardado con exito")

        case "G":
            convertir_campos_a_float(lista_superheroes)
            auxiliar_promedio_calculado = calcular_altura_promedio(lista_superheroes,"M")
            mostrar_promedio(auxiliar_promedio_calculado,"El promedio de altura de los superheroes masculinos es: ")

        case "H":
            convertir_campos_a_float(lista_superheroes)
            auxiliar_promedio_calculado = calcular_altura_promedio(lista_superheroes,"F")
            mostrar_promedio(auxiliar_promedio_calculado,"El promedio de altura de los superheroes femeninos es: ")

        case "I":
            if (len(lista_alturas_obtenidas) == 0):
                print("Por favor realice algun calculo de C a F para poder mostrar los datos")
            else:
                convertir_campos_a_float(lista_superheroes)
                listar_superheroes(lista_alturas_obtenidas, " *** Lista de superheroes *** ")
        
        case "J":
            agregar_todos_los_valores_a_lista(lista_superheroes, lista_colores_ojos, "color_ojos")
        
            agregar_valores_filtrando(lista_colores_ojos_filtrados, lista_colores_ojos)

            print("Calculo realizado y guardado con exito")
                                        
        case "K":
            agregar_todos_los_valores_a_lista(lista_superheroes, lista_colores_pelo, "color_pelo")

            agregar_valores_filtrando(lista_colores_pelo_filtrados, lista_colores_pelo)

            print("Calculo realizado y guardado con exito")

        case "L":

            agregar_todos_los_valores_a_lista(lista_superheroes, lista_tipo_inteligencia, "inteligencia")

            agregar_valores_filtrando(lista_tipo_inteligencia_filtrados, lista_tipo_inteligencia)

            print("Calculo realizado y guardado con exito")

        case "M":
            if (len(lista_colores_ojos_filtrados) == 0):

                print("Por favor realice el calculo de la opcion j")
            else:
                print("Superheroes filtrados por color de ojos")

                mostrar_heroes_filtrando_por_algun_valor(lista_colores_ojos_filtrados, lista_superheroes, "color_ojos")

        case "N":

            if (len(lista_colores_pelo_filtrados) == 0):
                
                print("Por favor realice el calculo de la opcion k")
            else:
                print("Superheroes filtrados por color de pelo")

                mostrar_heroes_filtrando_por_algun_valor(lista_colores_pelo_filtrados, lista_superheroes, "color_pelo")

        case "O":

            if (len(lista_tipo_inteligencia_filtrados) == 0):
                
                print("Por favor realice el calculo de la opcion L")
            else:
                print("Superheroes filtrados por tipo de inteligencia")

                mostrar_heroes_filtrando_por_algun_valor(lista_tipo_inteligencia_filtrados, lista_superheroes, "inteligencia")

        case "P":
            respuesta_seleccionada = input("Esta seguro que desea salir?(s-n): ")
            if(respuesta_seleccionada == "s"):
                print("Adios!")
                break

        case other:
            print("Por favor, ingrese una opcion valida")
            