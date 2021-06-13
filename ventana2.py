from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

filtro=1
tipo=0

ventana2=Tk()

frame2=Frame(ventana2)
frame2.pack()

n=IntVar()
fs=DoubleVar()
fc=DoubleVar()
fc1=DoubleVar()
fc2=DoubleVar()
rp=DoubleVar()
rs=DoubleVar()
n.set(0)
fs.set(0)
fc.set(0)
fc1.set(0)
fc2.set(0)
rp.set(0)
rs.set(0)

def salir():
    ventana2.destroy()

def limpiar():
    n.set(0)
    fs.set(0)
    fc.set(0)
    fc1.set(0)
    fc2.set(0)
    rp.set(0)
    rs.set(0)

def evaluar(filtro,tipo):			
	Fs=fs.get()/2

	if tipo==0:
		btype="lowpass"
		w=fc.get()/Fs
	elif tipo==1:
		btype="highpass"
		w=fc.get()/Fs
	elif tipo==2:
		btype="bandpass"
		w=[fc1.get()/Fs,fc2.get()/Fs]
	elif tipo==3:
		btype="bandstop"
		w=[fc1.get()/Fs,fc2.get()/Fs]
			
	if filtro==0:
		b,a=signal.butter(n.get(),w,btype)
		w,h=signal.freqz(b,a)
		plt.title('Butterworth filter frequency response')
	elif filtro==1:
		b,a=signal.butter(n.get(),rp.get(),w,btype)
		w,h=signal.freqz(b,a)
		plt.title('Chevyshev I filter frequency response')
	elif filtro==2:
		b,a=signal.butter(n.get(),rs.get(),w,btype)
		w,h=signal.freqz(b,a)
		plt.title('Chevyshev II filter frequency response')
	elif filtro==3:
		b,a=signal.butter(n.get(),rp.get(),rs.get(),w,btype)
		w,h=signal.freqz(b,a)
		plt.title('Elliptic filter frequency response')
	plt.semilogx(w,20*np.log10(abs(h)))
	plt.xlabel('Frequency [radians/second]')
	plt.ylabel('Amplitude [dB]')
	plt.margins(0,0.1)
	plt.grid(which='both',axis='both')
	plt.axvline(100,color='green')
	plt.show()

mostrar=Button(frame2,text="EVALUAR",width=10,command=lambda:evaluar(filtro,tipo))
mostrar.grid(row=7,column=1,padx=10,pady=10)

borrar=Button(frame2,text="BORRAR",width=10,command=limpiar)
borrar.grid(row=7,column=2,padx=10,pady=10)

exit=Button(frame2,text="SALIR",width=10,command=salir)
exit.grid(row=7,column=3,padx=10,pady=10)

labelN=Label(frame2,text="Orden del filtro:")
labelN.grid(row=1,column=1)

entryN=Entry(frame2,textvariable=n)
entryN.grid(row=1,column=2,padx=10,pady=10)
entryN.config(justify="right")

labelfs=Label(frame2,text="Frecuencia de muestreo:")
labelfs.grid(row=2,column=1)

entryfs=Entry(frame2,textvariable=fs)
entryfs.grid(row=2,column=2,padx=10,pady=10)
entryfs.config(justify="right")

if tipo==0 or tipo==1:
	labelfc=Label(frame2,text="Frecuencia de corte:")
	labelfc.grid(row=3,column=1)

	entryfc=Entry(frame2,textvariable=fc)
	entryfc.grid(row=3,column=2,padx=10,pady=10)
	entryfc.config(justify="right")
		
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
		
if filtro == 0:
	ventana2.title("Filtro Butterworth")

elif filtro==1:
	ventana2.title("Filtro Chevyshev Tipo I")

	labelrp=Label(frame2,text="Rizo en la región de pasa banda:")
	labelrp.grid(row=5,column=1)

	entryrp=Entry(frame2,textvariable=rp)
	entryrp.grid(row=5,column=2,padx=10,pady=10)
	entryrp.config(justify="right")

elif filtro==2:
	ventana2.title("Filtro Chevyshev Tipo II")

	labelrs=Label(frame2,text="Rizo en la región de rechazo:")
	labelrs.grid(row=6,column=1)

	entryrs=Entry(frame2,textvariable=rs)
	entryrs.grid(row=6,column=2,padx=10,pady=10)
	entryrs.config(justify="right")

elif filtro==3:
	ventana2.title("Filtro Elíptico")

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