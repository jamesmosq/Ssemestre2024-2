#9. Menús (Menu)
from tkinter import Tk
root = Tk()
from tkinter import Menu
menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nuevo")
file_menu.add_command(label="Salir", command=root.quit)

root.mainloop()  # Inicia el bucle de eventos de la ventana
