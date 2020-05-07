import tkinter    #Importa la libreria para la interfaz grafica
import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO  

def getExample03(root, r, c):
    def Valor():          # Metodo que obtiene el valor del escalar en tiempo real
        selection = "Intensidad = " + str(var.get())
        labelintensidad.config(text = selection)
        led.ChangeDutyCycle(var.get())      # LED #1 = i
        root.after(1000,Valor)
    def IniciarPines():   #Metodo para iniciar lo pines que se utilizaran
        GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
        GPIO.setup(ledpwm, GPIO.OUT)  # Ponemos el pin GPIO nº7 como salida para el LED #1   
    ledpwm = 13           #Variable para identificar el GPIO 7
    IniciarPines()        #Llama al metodo que inicia los pines
    led = GPIO.PWM(ledpwm, 100)   # Creamos el objeto led pwm con 100 valores
    led.start(0)           # Iniciamos el objeto led a 0 del ciclo de trabajo (completamente apagado)
    frame = tkinter.Frame(root)
    frame.grid(row=r, column=c)            # Creamos una interfaz grafica     #Agrega la etiqueta a la interfaz
    var = tkinter.DoubleVar()      #Se define una variable double tkinter
    scale = tkinter.Scale( frame, variable = var ) # Creamos un elememto escalar
    scale.pack(anchor=tkinter.CENTER)#El administrador de la interfaz agreaga el escalar
    labelintensidad = tkinter.Label(frame)#Se define una etiqueta para desplegar dunamicamente la intensidad 
    labelintensidad.pack()   #Agrega la etiqueta a la interfaz grafica
    Valor()                  #Metodo que se ejecuta automaticamente cada segundo y obtiene el valor del escalar


