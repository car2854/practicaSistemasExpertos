import math

from view import View

from nodo import Nodo

radio = 20


class Controlador:

    def __init__(self):
        self.dato = None
        self.nodoSeleccionado = None
        self.mousePress = False

    def movimientoMouse(self, event, lista, vista):
        if (event.state == 264 and self.nodoSeleccionado != None and not self.mousePress):
            self.mousePress = True

        if (event.state == 8 and self.nodoSeleccionado != None and self.mousePress):
            nodoDestino = None
            colision = False
            for i in lista:
                colision = self.colision([event.x,event.y],i.coordenadas[:], True)
                if (colision):
                    nodoDestino = i
                    break

            if (colision and self.nodoSeleccionado != nodoDestino):
                self.nodoSeleccionado.aristaPadre = nodoDestino
                nodoDestino.aristaHijo = self.nodoSeleccionado
                self.redibujar(lista,vista)
                
            self.mousePress = False
            self.nodoSeleccionado = None



    def seleccionar(self, event, lista, vista):
        colision = False
        if (len(lista) > 0):
            for i in lista:
                colision = self.colision([event.x,event.y],i.coordenadas[:], True)
                i.selected = False                
                if (colision):
                    i.selected = True
                    self.nodoSeleccionado = i
                self.redibujar(lista,vista)


    def agregar(self, event, lista, vista):
        colision = False
        coordenadas = [event.x,event.y]
        for i in lista:
            colision = self.colision(coordenadas,i.coordenadas)
            if (colision):
                break
        if (not colision):
            nodo = Nodo([event.x,event.y])
            lista.append(nodo)
            self.redibujar(lista,vista)

    def colision(self,coordenada1,coordenada2, select = False):
        xr = (coordenada1[0] - coordenada2[0]) * (coordenada1[0] - coordenada2[0])
        yr = (coordenada1[1] - coordenada2[1]) * (coordenada1[1] - coordenada2[1])
        distancia = math.sqrt(xr+yr)
        if (select):
            radioT = radio
        else:
            radioT = radio * 4
        if (distancia < radioT):
            return True
        return False

    def clear(self, lista, vista):
        lista.clear()
        vista.clear()

    def mostrarMensaje(self, vista):
        vista.mensaje("Info","Archivo Guardado")

    def redibujar(self, lista, vista):
        vista.clear()
        for i in lista:

            if (i.aristaPadre):
                partida = [i.coordenadas[0], i.coordenadas[1]]
                padre = i.aristaPadre
                destino = [padre.coordenadas[0], padre.coordenadas[1]]
                vista.dibujarArista(partida,destino)
            
            if (i.selected):
                coordenada1 = [i.coordenadas[0] - radio, i.coordenadas[1] - radio]
                coordenada2 = [i.coordenadas[0] + radio, i.coordenadas[1] + radio]
                colorBorder = "#148301"
                colorBody = "#1f1"
                vista.dibujarNodo(coordenada1, coordenada2, colorBorder, colorBody)   
            else:
                coordenada1 = [i.coordenadas[0] - radio, i.coordenadas[1] - radio]
                coordenada2 = [i.coordenadas[0] + radio, i.coordenadas[1] + radio]
                colorBorder = "#f11"
                colorBody = "#1f1"
                vista.dibujarNodo(coordenada1, coordenada2, colorBorder, colorBody)   

            

