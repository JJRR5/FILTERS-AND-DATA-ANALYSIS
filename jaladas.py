from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
def select():
    filtro=menu1.current() #dato acutal elegido
    print(filtro)
ventana=Tk()
ventana.title("Proyecto: Generación de filtros digitales")

frame=Frame(ventana)
frame.pack()
label1=Label(frame,text="Filtro:")
label1.grid(row=1,column=1)

menu1=ttk.Combobox(frame)
menu1.grid(row=1,column=2)
opciones1=["Butterworth","Chevyshev tipo I","Chevyshev tipo II","Elíptico"]
menu1["values"]=opciones1
botonselect=Button(frame,text="Seleccionar",width=10,command=select)
botonselect.grid(row=3,column=2,padx=10,pady=10)

ventana.mainloop()