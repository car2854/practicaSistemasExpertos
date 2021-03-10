from tkinter import *
from tkinter.messagebox import showinfo

from view import View
from controllers import Controlador

# Configuración de la raíz
root = Tk()

# Elementos Lista
lista = []

# Vista
data = View(root)

# Controlador
controller = Controlador()

root.geometry("600x400")

# ------------------------ MenuBar ------------------------------------
menubar = Menu(root)
root.config(menu=menubar)


# ------------------------ MenuOptions ------------------------------------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=lambda: controller.clear(lista, data))
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar", command=lambda: controller.mostrarMensaje(data))
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Como funciona?")

runmenu = Menu(menubar, tearoff=0)
runmenu.add_command(label="Run")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
menubar.add_cascade(label="Ejecutar", menu=runmenu)


# -------------------------- Title ----------------------------------
titulo = Label(root, text = "Sistema Experto")
titulo.pack(fill=X)

# -------------------------- Canva ----------------------------------
canvas = Canvas(width=400, height=300, bg='cyan')
data.agregarCanva(canvas)

# -------------------------- Event Click -----------------------------
# Click derecho
canvas.bind("<Button-3>", lambda event: controller.agregar(event, lista, data))

# Click izquierdo
canvas.bind("<Button-1>", lambda event: controller.seleccionar(event, lista, data))

#Evento del controller
canvas.bind("<Motion>", lambda event: controller.movimientoMouse(event, lista, data))


canvas.pack(expand=YES, fill=BOTH)



# Finalmente bucle de la aplicación
root.mainloop()

