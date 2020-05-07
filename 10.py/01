import RPi.GPIO as GPIO # Cargamos la biblioteca RPi.GPIO  
from tkinter import *   #Importamos la biblioteca para la interfaz grafica

def Ledonoff():         #Este metodo se ejecutara cuado el usuario presione en boton
    global prendido     # Variable booleana definida en el programa principal
    prendido=not prendido #Cambia de True a False y viceversa
    GPIO.output(gpiopin,prendido)# Enciende o apaga el Led conectado al gpio7

gpiopin = 18            #Variable para identificar al pin gpio 18 o fisico |1O.
GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
GPIO.setup(gpiopin, GPIO.OUT)  # Ponemos el pin nº18 como salida para el LED #1
root = Tk()             #Se  crea una interfaz grafica
prendido=False          #Variable booleana que permitira la orden de prender o apagar el Led
btn_led = Button(root, text="Led", command=Ledonoff) #Agrega un boton ala interfaz grafica con el texto Led y ejecutara el metodo Ledonoff cuando se presione el boton
btn_led.pack()          #Adminitrador de elementos que agrega secuencialmente elementos a la GUI. En este caso el boton el boton a la interfaz
root.mainloop()         #Ejecuta la interfaz grafica
GPIO.cleanup()          #libera el pin gpio7 al cerrar la interfaz grafica

