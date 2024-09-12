#11. Cuadro combinado (Combobox)
from tkinter import Tk
root = Tk()
from tkinter.ttk import Combobox
combo = Combobox(root, values=["Opción 1", "Opción 2", "Opción 3"])
combo.pack()
root.mainloop()  # Inicia el bucle de eventos de la ventana
