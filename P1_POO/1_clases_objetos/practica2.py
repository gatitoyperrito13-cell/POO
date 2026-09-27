"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
class Coches:
    def __init__(self, color, marca, velocidad):
        self.__color = color
        self.__marca = marca
        self.__velociadad = velocidad

    def acelerar(self):
        self.__velociadad+=1

    def frenar(self):
        self.__velociadad-=1

    def tocar_claxon(self):
        print("pip pip")

coche1 = Coches("Blanco", "VW", "220")
coche2 = Coches("Azul", "Nissan", "180")

#NO se puede sin no esta publico el atributo
# print("el color del coche 1 es ", coche1.__color)

#print("el coche uno con el claxon hace ", coche1.tocar_claxon())
# print(" ")
# print("El coche dos al tocar el clachon hace")
# coche2.tocar_claxon()

# coche1.acelerar()
# print("EL coche acelero y su velocidad ahora es de ", coche1.__velociadad)

#Instanciar o crear objetos de la clase Coches







