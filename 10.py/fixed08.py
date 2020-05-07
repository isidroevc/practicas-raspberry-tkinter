import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO  
import tkinter as tk
import time
from tkinter import Canvas

def getExample08(root, r, c):
	def Hcsr04():
		GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  #Configuramos Trigger como salida
		GPIO.setup(GPIO_ECHO,GPIO.IN)      #Configuramos Echo como entrada
		GPIO.output(GPIO_TRIGGER,False)    #Ponemos el pin 23 como LOW
		GPIO.output(GPIO_TRIGGER,True)   #Enviamos un pulso de ultrasonidos
		time.sleep(0.00001)              #Una pequeñña pausa
		GPIO.output(GPIO_TRIGGER,False)  #Apagamos el pulso
		start = time.time()              #Guarda el tiempo actual mediante time.time()
		while GPIO.input(GPIO_ECHO)==0:  #Mientras el sensor no reciba señal...
			start = time.time()          #Mantenemos el tiempo actual mediante time.time()
		while GPIO.input(GPIO_ECHO)==1:  #Si el sensor recibe señal...
			stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable
		elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envío y recepción
		distance = (elapsed * 34300)/2   #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
		print ("Distancia ",distance)#Devolvemos la distancia (en centímetros) por pantalla
		if distance>100:
			distance=100
		for i in range(0,100,10):
			canvasdistancia.create_arc(200-i, 200-i, 10+i, 10+i, start=315, extent=90, fill='green')
		canvasdistancia.create_arc(100+distance, 100+distance, 110-distance, 110-distance, start=315, extent=90,fill='red')
		selection = "Distancia = " + str(distance)
		labeldistancia.config(text = selection)
		root.after(1000,Hcsr04)                    #Pequeña pausa para no saturar el procesador de la Raspberry
	def IniciarPines():
		GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
        
	GPIO_TRIGGER = 23          #Usamos el pin GPIO 23 como TRIGGER
	GPIO_ECHO = 24
	IniciarPines()
	frame = tk.Frame(root)
	frame.grid(row=r, column=c)
	canvasdistancia = Canvas(frame)
	canvasdistancia.pack()
	labeldistancia = tk.Label(frame)
	labeldistancia.pack()
	Hcsr04()
