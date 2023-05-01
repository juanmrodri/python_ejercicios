def calcular_altura_promedio(lista:list, genero:str)->float:

    """Calcula el promedio de alturas

    Returns:
        _type_: _description_
    """
    
    cantidad_superheroes = 0
    acumulador_alturas = 0
    promedio_calculado = 0

    genero = genero.capitalize() # por si llega a venir una minuscula, igual esta hardcodeado aca

    if genero == "M":

        for superheroe in lista:

            if superheroe['genero'] == "M":

                cantidad_superheroes = cantidad_superheroes+1
                acumulador_alturas = acumulador_alturas + superheroe['altura']

    elif genero == "F":

        for superheroe in lista:

            if superheroe['genero'] == "F":

                cantidad_superheroes = cantidad_superheroes+1
                acumulador_alturas = acumulador_alturas + superheroe['altura']

    promedio_calculado = calcular_promedio(cantidad_superheroes,acumulador_alturas)

    return promedio_calculado