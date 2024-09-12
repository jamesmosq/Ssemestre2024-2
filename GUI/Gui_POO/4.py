#4. Entradas de texto (Entry)
from tkinter import Tk
root = Tk()
root.geometry('400x200')
from tkinter import Entry
entry = Entry(root)
entry.pack()
root.mainloop()  # Inicia el bucle de eventos de la ventana