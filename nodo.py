class Nodo:

    def __init__(self, coordenadas, selected = False):
        self.coordenadas = coordenadas
        self.selected = selected
        self.aristaPadre = None
        self.aristaHijo = None
        self.valor = None


class Arista:

    def __init__(self, nodoPadre, probabilidad):
        self.aristaPadre = nodoPadre
        self.probabilidad = probabilidad