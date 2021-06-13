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
	filtro=menu1.current() #dato acutal elegido
	tipo=menu2.current() #dato actual elegido x2	
	if filtro>=0 and tipo>=0:
		ventana2=Tk()
		frame2=Frame(ventana2)
		frame2.pack()
		#////////////FUNCIONES/////////////////////////////
		#SALIR()///////////////////
		def salir():
			ventana.destroy()
			ventana2.destroy()
		#LIMPIAR()//////////////////
		def limpiar():
			entryN.delete(0,END)
			entryfs.delete(0,END)
			entryfc.delete(0,END)
			entryfc1.delete(0,END)
			entryfc2.delete(0,END)
			entryrp.delete(0,END)
			entryrs.delete(0,END)

		def evaluar(filtro,tipo):
			n=int(entryN.get())
			fs=int(entryfs.get())
			#Logica para las variables 
			if filtro == 0 and tipo ==0 or tipo == 1: 
				fc=int(entryfc.get())
			elif filtro == 0 and tipo ==2 or tipo ==3: 
				fc1=int(entryfc1.get())
				fc2=int(entryfc2.get())
			elif filtro ==  1 and tipo==2 or tipo ==3:
				fc1=int(entryfc1.get())
				fc2=int(entryfc2.get())
				rp=int(entryrp.get())
			elif filtro == 1 and tipo ==0 or tipo ==1: 
				fc=int(entryfc.get())
				rp=int(entryrp.get())
			elif filtro == 2 and tipo ==0 or tipo == 1: 
				fc=int(entryfc.get())
				rs=int(entryrs.get())
			elif filtro ==  2 and tipo==2 or tipo ==3:
				fc1=int(entryfc1.get())
				fc2=int(entryfc2.get())
				rs=int(entryrp.get())
			elif filtro == 3 and tipo ==0 or tipo == 1: 
				fc=int(entryfc.get())
				rp=int(entryrp.get())
				rs=int(entryrp.get())
			elif filtro == 3 and tipo ==2 or tipo == 3: 
				fc1=int(entryfc1.get())
				fc2=int(entryfc2.get())
				rp=int(entryrp.get())
				rs=int(entryrp.get())
			Fs=fs/2
			if tipo==0:
				btype="lowpass"
				w=fc/Fs
			elif tipo==1:
				btype="highpass"
				w=fc/Fs
			elif tipo==2:
				btype="bandpass"
				w=[fc1/Fs,fc2/Fs]
			elif tipo==3:
				btype="bandstop"
				w=[fc1/Fs,fc2/Fs]
			
			if filtro==0:
				b,a=signal.butter(n,w,btype)
				w,h=signal.freqz(b,a)
				plt.title('Butterworth filter frequency response')
			elif filtro==1:
				b,a=signal.butter(n,rp,w,btype)
				w,h=signal.freqz(b,a)
				plt.title('Chevyshev I filter frequency response')
			elif filtro==2:
				b,a=signal.butter(n,rs,w,btype)
				w,h=signal.freqz(b,a)
				plt.title('Chevyshev II filter frequency response')
			elif filtro==3:
				b,a=signal.butter(n,rp,rs,w,btype)
				w,h=signal.freqz(b,a)
				plt.title('Elliptic filter frequency response')

			plt.semilogx(w,20*np.log10(abs(h)))
			plt.xlabel('Frequency [radians/second]')
			plt.ylabel('Amplitude [dB]')
			plt.margins(0,0.1)
			plt.grid(which='both',axis='both')
			plt.axvline(100,color='green')
			plt.show()
			
		#/////////////////////////////////////////
		#BOTONES VENTANA 2 
		#MOSTRAR RESPUESTA 
		mostrar=Button(frame2,text="EVALUAR",width=10,command=lambda:evaluar(filtro,tipo)) #esta funcion aun no se crea
		mostrar.grid(row=7,column=1,padx=10,pady=10)
		#LIMPIAR ENTRADAS
		limpiar=Button(frame2,text="BORRAR",width=10,command=limpiar)
		limpiar.grid(row=7,column=2,padx=10,pady=10)
		# SALIR DEL DISEÑO 
		salir=Button(frame2,text="SALIR",width=10,command=salir)
		salir.grid(row=7,column=3,padx=10,pady=10)
	#////////////////////////////////////////////////////////

		#Orden y frecuencia de muestreo (Todos la necesitan)
		
		labelN=Label(frame2,text="Orden del filtro:")
		labelN.grid(row=1,column=1)

		entryN=Entry(frame2)
		entryN.grid(row=1,column=2,padx=10,pady=10) #entry
		entryN.config(justify="right")

		labelfs=Label(frame2,text="Frecuencia de muestreo:")
		labelfs.grid(row=2,column=1)

		entryfs=Entry(frame2)
		entryfs.grid(row=2,column=2,padx=10,pady=10) #entry 
		entryfs.config(justify="right")

		#Frecuencia de corte para pasa bajas y pasa altas

		if tipo==0 or tipo==1:
			labelfc=Label(frame2,text="Frecuencia de corte:")
			labelfc.grid(row=3,column=1)

			entryfc=Entry(frame2)
			entryfc.grid(row=3,column=2,padx=10,pady=10)
			entryfc.config(justify="right")

		#Frecuencias de corte para pasa banda y rechazo de banda
		
		elif tipo==2 or tipo==3:
			labelfc1=Label(frame2,text="Frecuencia de corte inferior:")
			labelfc1.grid(row=3,column=1)

			entryfc1=Entry(frame2)
			entryfc1.grid(row=3,column=2,padx=10,pady=10)
			entryfc1.config(justify="right")

			labelfc2=Label(frame2,text="Frecuencia de corte superior:")
			labelfc2.grid(row=4,column=1)

			entryfc2=Entry(frame2)
			entryfc2.grid(row=4,column=2,padx=10,pady=10)
			entryfc2.config(justify="right")
		
		if filtro == 0:
			ventana2.title("Filtro Butterworth")

		#Filtro cheby1

		elif filtro==1:
			ventana2.title("Filtro Chevyshev Tipo I")

			labelrp=Label(frame2,text="Rizo en la región de pasa banda:")
			labelrp.grid(row=5,column=1)

			entryrp=Entry(frame2)
			entryrp.grid(row=5,column=2,padx=10,pady=10)
			entryrp.config(justify="right")

		#Filtro cheby2

		elif filtro==2:
			ventana2.title("Filtro Chevyshev Tipo II")

			labelrs=Label(frame2,text="Rizo en la región de rechazo:")
			labelrs.grid(row=6,column=1)

			entryrs=Entry(frame2)
			entryrs.grid(row=6,column=2,padx=10,pady=10)
			entryrs.config(justify="right")

		#Filtro ellip

		elif filtro==3:
			ventana2.title("Filtro Elíptico")

			labelrp=Label(frame2,text="Rizo en la región de pasa banda:")
			labelrp.grid(row=5,column=1)

			entryrp=Entry(frame2)
			entryrp.grid(row=5,column=2,padx=10,pady=10)
			entryrp.config(justify="right")

			labelrs=Label(frame2,text="Rizo en la región de rechazo:")
			labelrs.grid(row=6,column=1)

			entryrs=Entry(frame2)
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