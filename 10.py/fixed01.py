import tkinter
import RPi.GPIO as GPIO # Cargamos la biblioteca RPi.GPIO 
prendido = False
def getExample01(root, r, c):
	
	def Ledonoff():
		global prendido
		prendido=not prendido #Cambia de True a False y viceversa
		GPIO.output(gpiopin,prendido)# Enciende o apaga el Led conectado al gpio7

	gpiopin = 15            #Variable para identificar al pin gpio 18 o fisico |1O.
	GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
	GPIO.setup(gpiopin, GPIO.OUT)  # Ponemos el pin nº18 como salida para el LED #1
	frame = tkinter.Frame(root)
	frame.grid(row=r, column=c)           #Se  crea una interfaz grafica
	prendido=False          #Variable booleana que permitira la orden de prender o apagar el Led
	btn_led = tkinter.Button(frame, text="Led", command=Ledonoff) #Agrega un boton ala interfaz grafica con el texto Led y ejecutara el metodo Ledonoff cuando se presione el boton
	btn_led.pack()          #Adminitrador de elementos que agrega secuencialmente elementos a la GUI. En este caso el boton el boton a la interfaz 
