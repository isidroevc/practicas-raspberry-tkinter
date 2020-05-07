from tkinter import *      #Importa la libreria para la interfaz grafica
import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO

def Sel():
    selection = "Intensidad = " + str(var.get())
    labelintensidad.config(text = selection)
    led.ChangeDutyCycle(var.get())      # LED #1 = i

gpiopin=18
GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
GPIO.setup(gpiopin, GPIO.OUT)  # Ponemos el pin nº26 como salida para el LED #1
led = GPIO.PWM(gpiopin, 100)   # Creamos el objeto 'white' en el pin 25 a 100 Hz
led.start(0)# Iniciamos el objeto 'white' al 0% del ciclo de trabajo (completamente apagado)
root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=Sel)
button.pack(anchor=CENTER)

labelintensidad = Label(root)
labelintensidad.pack()

root.mainloop()
GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
GPIO.setup(gpiopin, GPIO.OUT)  # Ponemos el pin nº26 como salida para el LED #1
GPIO.cleanup()
