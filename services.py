import math

# from view import View

from nodo import Nodo, Arista

class Services:

    def __init__(self):
        self.aristas = []

    def guardar(self, value):
        pos = 0
        for i in value:
            if (float(i.get()) > 1):
                return "No se puede ingresar valores mayor a 1"

            if (float(i.get()) < 0.0):
                return "No se permiten valores negativos"

            self.aristas[pos].probabilidad = float(i.get())
            pos = pos + 1

        return "Los datos fueron guardados con exito"
        
