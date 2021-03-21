class Nodo:

    def __init__(self, coordenadas, id, type):
        self.coordenadas = coordenadas
        self.selected = False
        self.aristaPadre = []
        self.aristaHijo = []
        self.valor = None
        self.name = ""
        self.id = type + str(id)
        self.cf = -1


    def agregarPadre(self, arista):
        # arista = Arista(nodo, probabilidad)
        self.aristaPadre.append(arista)

    def agregarHijo(self, nodo):
        self.aristaHijo.append(nodo)

    def cambiarId(self, type, id):
        self.id = type + str(id)

class Arista:

    def __init__(self, nodoPadre, probabilidad):
        self.aristaPadre = nodoPadre
        self.probabilidad = probabilidad