import tkinter
from gpiozero import Buzzer #Cargamos la libreria para el buzzer
import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO 
def getExample04(root, r, c):
    def RuidoBuzzer():      #Metodo para iniciar y detener el ruido del buzzer
        global bz
        global ruido
        if ruido:
            bz.off()        #Apaga el ruido
        else:
            bz.on()         #enciende el ruido
        ruido=not ruido

    def IniciarPines():
        GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
        GPIO.setup(gpiobuzzer, GPIO.OUT)  # Ponemos el pin GPIO nº16 como salida para el LED #1
    gpiobuzzer=16          #Variable que especifica el pin que se utilizara
    IniciarPines()         #Iniciamos los pines a utilizar
    bz=Buzzer(gpiobuzzer)  #Creamos el buzzer
    ruido=False            #Variable boolena que permitira el encendido y apagado de buzzer
    frame = tkinter.Frame(root)
    frame.grid(row=r, column=c)           #Creamos la interfaz grafica
    btn_Buz16 = tkinter.Button(frame, text="RuidoBuzzer", command=RuidoBuzzer) # Creamos un boton para la interfaz grafica
    btn_Buz16.pack()        #Agregamos el boton a la interfaz
