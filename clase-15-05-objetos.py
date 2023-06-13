# objetos
# para las clases nomenclatura pascal case class PersonaBuena{}
# cuando una variable esta definida adentro de una clase, se llama atributo
# instancia es sinonimo de objeto, instanciar es crear un objeto
# el self, lo consigue python con el __init__, ya esta resuelto aca, en C se conseguia mediante el malloc
# si le ponemos __ a una variable atributo, eso la convierte en privada y no es accesible desde afuera
# para las anotation, los geters van primero
# @property le indica que el metodo es una propiedad, es un decorador, en geters se usa el @property, al setter, @nombre.setter (nombre del atributo, nombre de la funcion), ademas no lleva el nombre set_ o get_


# class Persona:

#     def __init__(self, id, nombre, apellido, edad) -> None:
        
#         self.id = id
#         self.nombre = nombre
#         self.apellido = apellido
#         self.__edad = edad
       
#     def set_edad(self, value):
#         if value > 0 and value < 100:
#             self.__edad = value

#     def get_edad(self):

#         return self.__edad
    
#per1 = Persona(10, "Jose", "Lopez", 30)

class Persona:

    def __init__(self, id, nombre, apellido, edad) -> None:
        
        self.id = id
        self.__nombre = nombre
        self.apellido = apellido
        self.__edad = edad


    def get_edad(self):

        return self.__edad

    def set_edad(self, value):
        if value > 0 and value < 100:
            self.__edad = value

    @property
    def nombre(self):

        return self.__nombre
    
    @nombre.setter
    def nombre(self, value: str):

        self.nombre = value


per1 = Persona(10, "Jose", "Lopez", 30)


print(per1.nombre)