from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox
from services import Services
from tkinter import simpledialog

from tkinter import filedialog as fd

class View:
    def __init__(self, root):
        self.root = root
        self.canvas = None
        self.save = Services()

    def dibujarNodo(self, coordenada1, coordenada2 ,colorBorder ,colorBody, id, coordenadaReal):
        self.canvas.create_oval(coordenada1[0],coordenada1[1],coordenada2[0],coordenada2[1], outline=colorBorder, fill=colorBody, width=2)
        self.canvas.create_text(coordenadaReal[0],coordenadaReal[1],fill="black",font="Times 10 bold",text=id)

    def dibujarArista(self, coordenada1, coordenada2, probabilidad):
        self.canvas.create_line(coordenada1[0], coordenada1[1], coordenada2[0], coordenada2[1],fill='#868687',arrow=LAST)
        xt = (coordenada1[0] + coordenada2[0]) / 2
        yt = (coordenada1[1] + coordenada2[1]) / 2
        self.canvas.create_text(xt,yt,fill="black",font="Times 10 bold",text=probabilidad)

    def clear(self):
        self.canvas.delete("all")

    def agregarCanva(self,canvas):
        self.canvas = canvas    

    def mensaje(self, vertice):
        # showinfo(title, text)
        value = simpledialog.askstring(title="Probabilidad",prompt="Cual es el valor de la probabilidad de la Arista: " + vertice.id)
        if (value == None or value==""):
            value = 0.0
        return float(value)



    def tools(self, sidebar, nodo):
        for widget in sidebar.winfo_children():
            widget.destroy()

        nombre_label= Label(sidebar, text="Id del Nodo " + nodo.id)
        nombre_label.grid(row=1, column=0)
        nombre_label.config(padx=57, pady=10)

        button1=Button(sidebar, text="Guardar", command = self.guardar)
        button1.grid(row=2,column=0)

        c = 3
        index = 0

        self.cuadroArista = []
        self.save.aristas = nodo.aristaPadre

        for i in nodo.aristaPadre:
            nombre_label= Label(sidebar, text="Probabilidad al Nodo " + i.aristaPadre.id)
            nombre_label.grid(row=c+1, column=0)
            nombre_label.config(padx=0, pady=10)
            self.cuadroArista.append(Entry(sidebar))
            self.cuadroArista[index].insert(0, i.probabilidad)
            self.cuadroArista[index].grid(row=c+2, column=0)
            c = c + 2
            index = index + 1


    def clearTools(self, sidebar):
        print("Limpiar")



    def guardar(self):
        mensaje = self.save.guardar(self.cuadroArista)
        msg = messagebox.showinfo( "Advertencia", mensaje)


    def helpModal(self):
        self.top = Toplevel(self.root)
        self.top.transient(self.root)
        self.top.grab_set()
        
        titleText = 'Como funciona?'
        Label(self.top, text=titleText).pack()
        
        # Paso 1
        title1 = 'Paso 1'
        content1 = 'Seleccione con el click derecho del mouse para agregar un nodo'
        Label(self.top, text=title1).pack()
        Label(self.top, text=content1).pack()

        # Paso 2
        title2 = 'Paso 2'
        content2 = 'Seleccione el nodo que quiera trabajar'
        Label(self.top, text=title2).pack()
        Label(self.top, text=content2).pack()
        
        # Paso 3
        title3 = 'Paso 3'
        content3 = 'Para crear una arista, debe tener seleccionado el nodo y arrastrarlo hasta el siguiente nodo'
        Label(self.top, text=title3).pack()
        Label(self.top, text=content3).pack()
        
        # Paso 4
        title4 = 'Paso 4'
        content4 = 'Para agregar un valor a la arista, debe tener seleccionado el Nodo y en la parte izquierda de la pantalla puede ver las aristas del Nodo y agregar una probabilidad'
        Label(self.top, text=title4).pack()
        Label(self.top, text=content4).pack()
        
        # Paso 5
        title5 = 'Paso 5'
        content5 = 'Si quiere crear Meta, Hechos Nativos, etc. La aplicacion automaticamente determinara que clase de Nodo es, y pintara de diferente color los Nodos dependiendo si es Meta, Hechos Nativos, etc.'
        Label(self.top, text=title5).pack()
        Label(self.top, text=content5).pack()



    def saveDocument(self, saveDatos):
        nombrearch=fd.asksaveasfilename(initialdir = "C:/Users/Toshibaa/Desktop/python, proyecto",title = "Guardar como",filetypes = (("txt files","*.RB"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(saveDatos)
            archi1.close()

    def modalAlert(self,title,mensaje):
        messagebox.showinfo(message=mensaje, title=title)
            
            
