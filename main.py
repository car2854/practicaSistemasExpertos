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

root.wm_state("zoomed")
root.resizable(0,0)

# ------------------------ MenuBar ------------------------------------
menubar = Menu(root)
root.config(menu=menubar)



# ------------------------ Controlador ------------------------------------
controller = Controlador(root)

# ------------------------ MenuOptions ------------------------------------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=lambda: controller.clear(lista, data))
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar", command=lambda: controller.guardar(data, lista))
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Como funciona?", command=lambda: data.helpModal())

runmenu = Menu(menubar, tearoff=0)
runmenu.add_command(label="Run", command=lambda: controller.run(lista, data))

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
menubar.add_cascade(label="Ejecutar", menu=runmenu)


# -------------------------- Title ----------------------------------
titulo = Label(root, text = "Sistema Experto")
titulo.pack(fill=X)

# -------------------------- Sidebar ----------------------------------
sidebar = Frame(root, width=220, bg='white', height=300, relief='sunken', borderwidth=2)
sidebar.grid_propagate(False)
sidebar.pack(expand=False, fill='both', side='left')

# -------------------------- Canva ----------------------------------
canvas = Canvas(width=400, height=300, bg='cyan')
data.agregarCanva(canvas)

# -------------------------- Event Click -----------------------------
# Click derecho
canvas.bind("<Button-3>", lambda event: controller.agregar(event, lista, data))

# Click izquierdo
canvas.bind("<Button-1>", lambda event: controller.seleccionar(event, lista, data, sidebar))

#Evento del controller
canvas.bind("<Motion>", lambda event: controller.movimientoMouse(event, lista, data, sidebar))


canvas.pack(expand=YES, fill=BOTH)



# Finalmente bucle de la aplicación
root.mainloop()

