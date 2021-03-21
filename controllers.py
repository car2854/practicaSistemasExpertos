import math


from nodo import Nodo, Arista

radio = 20


class Controlador:

    def __init__(self, root):
        self.dato = None
        self.nodoSeleccionado = None
        self.mousePress = False
        self.idInit = 1
        self.idBody = 1
        self.idEnd = 1
        self.root = root

    def movimientoMouse(self, event, lista, vista, sidebar):

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
                nodoPadres = self.nodoSeleccionado.aristaPadre
                existe = False
                for padre in nodoPadres:
                    if (padre.aristaPadre == nodoDestino):
                        existe = True
                        break
                
                if (not existe):
                    arista = Arista(nodoDestino, 0.0)
                    self.nodoSeleccionado.agregarPadre(arista)
                    nodoDestino.agregarHijo(self.nodoSeleccionado)

                    if (len(nodoDestino.aristaHijo) > 0 and len(nodoDestino.aristaPadre) > 0):
                        nodoDestino.cambiarId("B",self.idBody)
                        self.idBody = self.idBody + 1

                    
                    if (len(nodoDestino.aristaHijo) > 0 and len(nodoDestino.aristaPadre) == 0):
                        nodoDestino.cambiarId("M",self.idEnd)
                        self.idEnd = self.idEnd + 1

# --------------------------------------------------- Mejorar Codigo ---------------------------------------------------
                if (len(self.nodoSeleccionado.aristaHijo) > 0 and len(self.nodoSeleccionado.aristaPadre) > 0):
                    self.nodoSeleccionado.cambiarId("B",self.idBody)
                    self.idBody = self.idBody + 1
                
                if (len(self.nodoSeleccionado.aristaHijo) > 0 and len(self.nodoSeleccionado.aristaPadre) == 0):
                    self.nodoSeleccionado.cambiarId("M",self.idEnd)
                    self.idEnd = self.idEnd + 1
# --------------------------------------------------------- Fin ---------------------------------------------------------

                self.redibujar(lista,vista)
                vista.tools(sidebar, self.nodoSeleccionado)
                
            self.mousePress = False
            self.nodoSeleccionado = None



    def seleccionar(self, event, lista, vista, sidebar):
        colision = False
        if (len(lista) > 0):
            for i in lista:
                colision = self.colision([event.x,event.y],i.coordenadas[:], True)
                i.selected = False                
                if (colision):
                    i.selected = True
                    self.nodoSeleccionado = i
                    vista.tools(sidebar, i)
                self.redibujar(lista,vista)
            

    def agregar(self, event, lista, vista):
        colision = False
        coordenadas = [event.x,event.y]
        for i in lista:
            colision = self.colision(coordenadas,i.coordenadas)
            if (colision):
                break
        if (not colision):
            nodo = Nodo([event.x,event.y], self.idInit, "H")
            self.idInit = self.idInit + 1
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

            if (len(i.aristaPadre) > 0):
                for padre in i.aristaPadre:
                    partida = [i.coordenadas[0], i.coordenadas[1]]
                    destino = [padre.aristaPadre.coordenadas[0], padre.aristaPadre.coordenadas[1]]

                    screen_width = self.root.winfo_screenwidth()
                    screen_height = self.root.winfo_screenheight()

                    disX = destino[0] - partida[0]
                    disY = destino[1] - partida[1]
                    disy = disY * -1

                    a=math.sqrt((disX * disX) + (disY * disY) )

                    ux = destino[0] / a
                    uy = destino[1] / a

                    ux = ux * 15
                    uy = uy * 15

                    # destino[0] = destino[0] - ux
                    # destino[1] = destino[1] - uy

                    # print(ux,uy)
                    # print(destino)
                    # print(partida)

                    vista.dibujarArista(partida,destino,padre.probabilidad)


            colorBorder = "#000000"
            colorBody = "#1f1"
            coordenada1 = [i.coordenadas[0] - radio, i.coordenadas[1] - radio]
            coordenada2 = [i.coordenadas[0] + radio, i.coordenadas[1] + radio]
            coordenadaReal = [i.coordenadas[0], i.coordenadas[1]]
            
            if (i.selected):
                colorBorder = "#4DA099"

            if(i.id[0] == "H"):
                colorBody = "#9B78CB"

            if(i.id[0] == "M"):
                colorBody = "#66A89F"


            vista.dibujarNodo(coordenada1, coordenada2, colorBorder, colorBody, i.id, coordenadaReal)   




    def run(self,lista,vista):
        
        cantidadMetas = 0
        meta = None
        
        for i in lista:
            acumProb = -1
            if (i.id[0] == "M"):
                cantidadMetas = cantidadMetas + 1
                meta = i

            for hijo in i.aristaHijo:
                for aristas in hijo.aristaPadre:
                    if (aristas.aristaPadre == i):
                        if (acumProb == -1):
                            acumProb = 0
                        acumProb = acumProb + aristas.probabilidad

            if (acumProb != -1):
                if (acumProb != 1.0):
                    vista.modalAlert("Error","Error en la probabilidad del Nodo: " + i.id)
                    return


        if (cantidadMetas>1):
            vista.modalAlert("Error","existen mas de 1 Meta")
            return
        
        if (cantidadMetas==0):
            vista.modalAlert("Error","no tiene ninguna meta")
            return

        vista.modalAlert("Info","La probabilidad es: " + str(self.cf(meta,vista)))
        
        

# -------------------------------------Codigo-------------------------------------
    def cf(self,vertice,vista):
        if (self.isHecho(vertice)):
            if (vertice.cf == -1):
                return self.CFHecho(vertice,vista)
            else:
                return vertice.cf
        vertices = self.getAdy(vertice)
        ac = 0
        for i in vertices:
            if (i.cf == -1):
                i.cf = self.cf(i,vista)
            ac = ac + i.cf * self.prob(i,vertice)
        vertice.cf = ac
        return ac



    def CFHecho(self,vertice,vista):
        vertice.cf = vista.mensaje(vertice)
        return vertice.cf




    def prob(self, origen, destino):
        for i in origen.aristaPadre:
            if (i.aristaPadre == destino):
                return i.probabilidad



    def getAdy(self, vertice):
        return vertice.aristaHijo

    


    def isHecho(self,nodo):
        return (nodo.id[0] == 'H')




    def guardar(self, vista, lista):

        saveDocument = ''
        for i in lista:
            saveNodo = 'coor: '
            saveNodo = '' + str(i.coordenadas[0]) + ',' + str(i.coordenadas[1])
        print(saveDocument)
        # vista.saveDocument(lista)
        vista.mensaje("Info","Archivo Guardado")
