import tkinter
import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO 
from gpiozero import AngularServo
abierto=False
def getExample05(root, r, c):
    def ServoMotor():
        global abierto
        if abierto:
            sermot.angle=0
            servoEtqBoton="Abrir"
        else:
            sermot.angle=90
            servoEtqBoton="Cerrar"
        btn_servo.configure(text=servoEtqBoton)
        abierto=not abierto
    def IniciarPines():
        GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM
    gpioservo = 18
    IniciarPines()
    abierto=False
    sermot=AngularServo(gpioservo)
    frame=tkinter.Frame(root)
    frame.grid(row=r, column=c)
    btn_servo = tkinter.Button(frame, text="Abrir", command=ServoMotor)
    btn_servo.pack(anchor=tkinter.CENTER)
