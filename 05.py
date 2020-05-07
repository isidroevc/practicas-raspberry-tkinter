import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO  
from tkinter import *
from gpiozero import AngularServo
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
gpioservo = 17
IniciarPines()
abierto=False
sermot=AngularServo(gpioservo)
root=Tk()
btn_servo = Button(root, text="Abrir", command=ServoMotor)
btn_servo.pack(anchor=CENTER)
root.mainloop()
GPIO.cleanup()          # Limpiamos los pines GPIO y salimos
