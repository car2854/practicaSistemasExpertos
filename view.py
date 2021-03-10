from tkinter import *
from tkinter.messagebox import showinfo

class View:
    def __init__(self, root):
        self.root = root
        self.canvas = None

    def dibujarNodo(self, coordenada1, coordenada2 ,colorBorder ,colorBody):
        self.canvas.create_oval(coordenada1[0],coordenada1[1],coordenada2[0],coordenada2[1], outline=colorBorder, fill=colorBody, width=2)

    def dibujarArista(self, coordenada1, coordenada2):
        self.canvas.create_line(coordenada1[0], coordenada1[1], coordenada2[0], coordenada2[1])


    def clear(self):
        self.canvas.delete("all")

    def agregarCanva(self,canvas):
        self.canvas = canvas    

    def mensaje(self, title, text):
        showinfo(title, text)