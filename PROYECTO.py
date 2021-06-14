from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

ventana=Tk()
ventana.title("Generación de filtros digitales")
ventana.geometry("500x120")
ventana.iconbitmap("jc.ico")
ventana.resizable(0,0)
ventana.config (bg='dark turquoise')
frame=Frame(ventana)
frame.pack()
frame.config(bg="dark turquoise")
frame.config(width="500",height="120",cursor='hand2')

#Segunda ventana

def select():
	filtro=menu1.current() #dato acutal elegido
	tipo=menu2.current() #dato actual elegido x2	
	if filtro>=0 and tipo>=0: 
		ventana2=Tk()
		ventana2.geometry("650x350")
		ventana2.iconbitmap("jc.ico")
		ventana2.config(bg='sky blue')
		ventana2.resizable(0,0)
		frame2=Frame(ventana2)
		frame2.pack()
		frame2.config(bg="sky blue",width="650",height="350",cursor='hand2')
		#////////////FUNCIONES/////////////////////////////
		#SALIR()///////////////////
		def salir1():
			ventana2.destroy()
		#LIMPIAR()//////////////////
		def limpiar():
			entryN.delete(0,END)
			entryfs.delete(0,END)
			try:
				entryfc.delete(0,END)
			except:
				entryfc1.delete(0,END)
				entryfc2.delete(0,END)
			try:
				entryfc1.delete(0,END)
				entryfc2.delete(0,END)
			except:
				entryfc.delete(0,END)
			try:
				entryrp.delete(0,END)
			except:
				entryN.delete(0,END)
				entryfs.delete(0,END)
			try:
				entryrs.delete(0,END)
			except:
				entryN.delete(0,END)
				entryfs.delete(0,END)

		def evaluar(filtro,tipo):
			try:
				
				n=int(entryN.get())
				fs=float(entryfs.get())
				#Logica para las variables
				if filtro == 0 and (tipo ==0 or tipo == 1): 
					fc=float(entryfc.get())
				elif filtro == 0 and (tipo ==2 or tipo ==3): 
					if int(entryfc1.get())>int(entryfc2.get()):
						messagebox.showerror(message="La frecuencia 1 debe ser menor a la 2",title="Error")
						tipo="nada"
					else:
						fc1=float(entryfc1.get())
						fc2=float(entryfc2.get())
				elif filtro ==  1 and (tipo==2 or tipo ==3):
					if int(entryfc1.get())>int(entryfc2.get()):
						messagebox.showerror(message="La frecuencia 1 debe ser menor a la 2",title="Error")
						tipo="nada"
					else:
						fc1=float(entryfc1.get())
						fc2=float(entryfc2.get())
						rp=float(entryrp.get())
				elif filtro == 1 and (tipo ==0 or tipo ==1): 
					fc=float(entryfc.get())
					rp=float(entryrp.get())
				elif filtro == 2 and (tipo ==0 or tipo == 1): 
					fc=float(entryfc.get())
					rs=float(entryrs.get())
				elif filtro ==  2 and (tipo==2 or tipo ==3):
					if int(entryfc1.get())>int(entryfc2.get()):
						messagebox.showerror(message="La frecuencia 1 debe ser menor a la 2",title="Error")
						tipo="nada"
					else:
						fc1=float(entryfc1.get())
						fc2=float(entryfc2.get())
						rs=float(entryrs.get())
				elif filtro == 3 and (tipo ==0 or tipo == 1): 
					fc=float(entryfc.get())
					rp=float(entryrp.get())
					rs=float(entryrp.get())
				elif filtro == 3 and (tipo ==2 or tipo == 3): 
					if int(entryfc1.get())>int(entryfc2.get()):
						messagebox.showerror(message="La frecuencia 1 debe ser menor a la 2",title="Error")
						tipo="nada"
					else:
						fc1=float(entryfc1.get())
						fc2=float(entryfc2.get())
						rp=float(entryrp.get())
						rs=float(entryrp.get())
				
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
					b,a=signal.cheby1(n,rp,w,btype)
					w,h=signal.freqz(b,a)
					plt.title('Chebyshev I filter frequency response')
				elif filtro==2:
					b,a=signal.cheby2(n,rs,w,btype)
					w,h=signal.freqz(b,a)
					plt.title('Chebyshev II filter frequency response')
				elif filtro==3:
					b,a=signal.ellip(n,rp,rs,w,btype)
					w,h=signal.freqz(b,a)
					plt.title('Elliptic filter frequency response')

				plt.semilogx(w,20*np.log10(abs(h)))
				plt.xlabel('Frequency [radians/second]')
				plt.ylabel('Amplitude [dB]')
				plt.margins(0,0.1)
				plt.grid(which='both',axis='both')
				plt.axvline(100,color='green')
				plt.show()
			except:
				messagebox.showerror(message="Favor de veificar los datos",title="Error")
		#/////////////////////////////////////////
		#BOTONES VENTANA 2 
		#MOSTRAR RESPUESTA 
		mostrar=Button(frame2,text="EVALUAR",width=10,command=lambda:evaluar(filtro,tipo),activebackground='lawn green',font="Arial 13")
		mostrar.grid(row=15,column=1,padx=10,pady=10)
		#LIMPIAR ENTRADAS
		borrar=Button(frame2,text="BORRAR",width=10,command=limpiar,activebackground='gold',font="Arial 13")
		borrar.grid(row=15,column=2,padx=10,pady=10)
		# SALIR DEL DISEÑO 
		out1=Button(frame2,text="SALIR",width=10,command=salir1,activebackground='red',font="Arial 13")
		out1.grid(row=15,column=3,padx=10,pady=10)
	#////////////////////////////////////////////////////////

		#Orden y frecuencia de muestreo (Todos la necesitan)
		
		labelN=Label(frame2,text="Orden del filtro:",font="Arial 13",bg='sky blue')
		labelN.grid(row=1,column=1)

		entryN=Entry(frame2,font="Arial 15")
		entryN.grid(row=1,column=2,padx=10,pady=10) #entry
		entryN.config(justify="right")

		labelfs=Label(frame2,text="Frecuencia de muestreo:",font="Arial 13",bg='sky blue')
		labelfs.grid(row=2,column=1)

		entryfs=Entry(frame2,font="Arial 15")
		entryfs.grid(row=2,column=2,padx=10,pady=10) #entry 
		entryfs.config(justify="right")

		#Frecuencia de corte para pasa bajas y pasa altas

		if tipo==0 or tipo==1:
			labelfc=Label(frame2,text="Frecuencia de corte:",font="Arial 13",bg='sky blue')
			labelfc.grid(row=3,column=1)

			entryfc=Entry(frame2,font="Arial 15")
			entryfc.grid(row=3,column=2,padx=10,pady=10)
			entryfc.config(justify="right")

		#Frecuencias de corte para pasa banda y rechazo de banda
		
		elif tipo==2 or tipo==3:
			labelfc1=Label(frame2,text="Frecuencia de corte inferior:",font="Arial 13",bg='sky blue')
			labelfc1.grid(row=3,column=1)

			entryfc1=Entry(frame2,font="Arial 15")
			entryfc1.grid(row=3,column=2,padx=10,pady=10)
			entryfc1.config(justify="right")

			labelfc2=Label(frame2,text="Frecuencia de corte superior:",font="Arial 13",bg='sky blue')
			labelfc2.grid(row=4,column=1)

			entryfc2=Entry(frame2,font="Arial 15")
			entryfc2.grid(row=4,column=2,padx=10,pady=10)
			entryfc2.config(justify="right")
		
		if filtro == 0:
			ventana2.title("Filtro Butterworth")

		#Filtro cheby1

		elif filtro==1:
			ventana2.title("Filtro Chevyshev Tipo I")

			labelrp=Label(frame2,text="Rizo en la región de pasa banda:",font="Arial 13",bg='sky blue')
			labelrp.grid(row=5,column=1)

			entryrp=Entry(frame2,font="Arial 15")
			entryrp.grid(row=5,column=2,padx=10,pady=10)
			entryrp.config(justify="right")

		#Filtro cheby2

		elif filtro==2:
			ventana2.title("Filtro Chevyshev Tipo II")

			labelrs=Label(frame2,text="Rizo en la región de rechazo:",font="Arial 13",bg='sky blue')
			labelrs.grid(row=6,column=1)

			entryrs=Entry(frame2,font="Arial 15")
			entryrs.grid(row=6,column=2,padx=10,pady=10)
			entryrs.config(justify="right")

		#Filtro ellip

		elif filtro==3:
			ventana2.title("Filtro Elíptico")

			labelrp=Label(frame2,text="Rizo en la región de pasa banda:",font="Arial 13",bg='sky blue')
			labelrp.grid(row=5,column=1)

			entryrp=Entry(frame2,font="Arial 15")
			entryrp.grid(row=5,column=2,padx=10,pady=10)
			entryrp.config(justify="right")

			labelrs=Label(frame2,text="Rizo en la región de rechazo:",font="Arial 13",bg='sky blue')
			labelrs.grid(row=6,column=1)

			entryrs=Entry(frame2,font="Arial 15")
			entryrs.grid(row=6,column=2,padx=10,pady=10)
			entryrs.config(justify="right")
			
		ventana2.mainloop()
	else:
		messagebox.showerror(message="Debes seleccionar un filtro y un tipo",title="Error")

def salir2():
	ventana.destroy()

label1=Label(frame,text="Filtro:",font="Arial 15",bg='dark turquoise')
label1.grid(row=1,column=1)

menu1=ttk.Combobox(frame,font="Arial 15")
menu1.grid(row=1,column=2)
opciones1=["Butterworth","Chebyshev tipo I","Chebyshev tipo II","Elíptico"]
menu1["values"]=opciones1

label2=Label(frame,text="Tipo:",font="Arial 15",bg='dark turquoise')
label2.grid(row=2,column=1)

menu2=ttk.Combobox(frame,font="Arial 15")
menu2.grid(row=2,column=2)
opciones2=["Pasa bajas","Pasa altas","Pasa banda","Rechazo de banda"]
menu2["values"]=opciones2

botonselect=Button(frame,text="Seleccionar",width=10,command=select,activebackground='lawn green',font="Arial 13")
botonselect.grid(row=10,column=3,padx=10,pady=10)

out2=Button(frame,text="Salir",width=10,command=salir2,activebackground="red",font="Arial 13")
out2.grid(row=10,column=1,padx=10,pady=10)

ventana.mainloop()