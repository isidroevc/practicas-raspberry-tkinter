import tkinter    #Importa la libreria para la interfaz grafica
import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO
def getExample02(root, r,c):
    def Sel():
        selection = "Intensidad = " + str(var.get())
        labelintensidad.config(text = selection)
        led.ChangeDutyCycle(var.get())      # LED #1 = i

    gpiopin=12
    GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
    GPIO.setup(gpiopin, GPIO.OUT)  # Ponemos el pin nº26 como salida para el LED #1
    led = GPIO.PWM(gpiopin, 100)   # Creamos el objeto 'white' en el pin 25 a 100 Hz
    led.start(0)# Iniciamos el objeto 'white' al 0% del ciclo de trabajo (completamente apagado)
    frame = tkinter.Frame(root)
    frame.grid(row=r, column=c)
    var = tkinter.DoubleVar()
    scale = tkinter.Scale( frame, variable = var )
    scale.pack(anchor=tkinter.CENTER)

    button = tkinter.Button(frame, text="Get Scale Value", command=Sel)
    button.pack(anchor=tkinter.CENTER)

    labelintensidad = tkinter.Label(frame)
    labelintensidad.pack()


    GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
    GPIO.setup(gpiopin, GPIO.OUT)  # Ponemos el pin nº26 como salida para el LED #1s

