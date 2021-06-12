from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

ventana=Tk()
ventana.title("Proyecto: Generación de filtros digitales")

frame=Frame(ventana)
frame.pack()

#Segunda ventana

def select():
	filtro=menu1.current()
	tipo=menu2.current()
	
	if filtro>=0 and tipo>=0:
		ventana2=Tk()
		ventana2.title("Proyecto: Generación de filtros digitales")
		
		frame2=Frame(ventana2)
		frame2.pack()

		N=IntVar()
		fs=DoubleVar()
		fc=DoubleVar()
		fc1=DoubleVar()
		fc2=DoubleVar()
		rp=DoubleVar()
		rs=DoubleVar()

		#Orden y frecuencia de muestreo (Todos la necesitan)
		
		labelN=Label(frame2,text="Orden del filtro:")
		labelN.grid(row=1,column=1)

		entryN=Entry(frame2,textvariable=N)
		entryN.grid(row=1,column=2,padx=10,pady=10)
		entryN.config(justify="right")

		labelfs=Label(frame2,text="Frecuencia de muestreo:")
		labelfs.grid(row=2,column=1)

		entryfs=Entry(frame2,textvariable=fs)
		entryfs.grid(row=2,column=2,padx=10,pady=10)
		entryfs.config(justify="right")

		#Frecuencia de corte para pasa bajas y pasa altas

		if tipo==0 or tipo==1:
			labelfc=Label(frame2,text="Frecuencia de corte:")
			labelfc.grid(row=3,column=1)

			entryfc=Entry(frame2,textvariable=fc)
			entryfc.grid(row=3,column=2,padx=10,pady=10)
			entryfc.config(justify="right")

		#Frecuencias de corte para pasa banda y rechazo de banda
		
		elif tipo==2 or tipo==3:
			labelfc1=Label(frame2,text="Frecuencia de corte inferior:")
			labelfc1.grid(row=3,column=1)

			entryfc1=Entry(frame2,textvariable=fc1)
			entryfc1.grid(row=3,column=2,padx=10,pady=10)
			entryfc1.config(justify="right")

			labelfc2=Label(frame2,text="Frecuencia de corte superior:")
			labelfc2.grid(row=4,column=1)

			entryfc2=Entry(frame2,textvariable=fc2)
			entryfc2.grid(row=4,column=2,padx=10,pady=10)
			entryfc2.config(justify="right")
		
		#Filtro cheby1

		if filtro==1:
			labelrp=Label(frame2,text="Rizo en la región de pasa banda:")
			labelrp.grid(row=5,column=1)

			entryrp=Entry(frame2,textvariable=rp)
			entryrp.grid(row=5,column=2,padx=10,pady=10)
			entryrp.config(justify="right")

		#Filtro cheby2

		elif filtro==2:
			labelrs=Label(frame2,text="Rizo en la región de rechazo:")
			labelrs.grid(row=6,column=1)

			entryrs=Entry(frame2,textvariable=rs)
			entryrs.grid(row=6,column=2,padx=10,pady=10)
			entryrs.config(justify="right")

		#Filtro ellip

		elif filtro==3:
			labelrp=Label(frame2,text="Rizo en la región de pasa banda:")
			labelrp.grid(row=5,column=1)

			entryrp=Entry(frame2,textvariable=rp)
			entryrp.grid(row=5,column=2,padx=10,pady=10)
			entryrp.config(justify="right")

			labelrs=Label(frame2,text="Rizo en la región de rechazo:")
			labelrs.grid(row=6,column=1)

			entryrs=Entry(frame2,textvariable=rs)
			entryrs.grid(row=6,column=2,padx=10,pady=10)
			entryrs.config(justify="right")
			
		ventana2.mainloop()
	else:
		messagebox.showerror(message="Debes seleccionar un filtro y un tipo",title="Error")

label1=Label(frame,text="Filtro:")
label1.grid(row=1,column=1)

menu1=ttk.Combobox(frame)
menu1.grid(row=1,column=2)
opciones1=["Butterworth","Chevyshev tipo I","Chevyshev tipo II","Elíptico"]
menu1["values"]=opciones1

label2=Label(frame,text="Tipo:")
label2.grid(row=2,column=1)

menu2=ttk.Combobox(frame)
menu2.grid(row=2,column=2)
opciones2=["Pasa bajas","Pasa altas","Pasa banda","Rechazo de banda"]
menu2["values"]=opciones2

botonselect=Button(frame,text="Seleccionar",width=10,command=select)
botonselect.grid(row=3,column=2,padx=10,pady=10)

ventana.mainloop()