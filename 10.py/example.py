import tkinter

def getExample01(root, r, c):
	frame = tkinter.Frame(root)
	frame.grid(row=r,column=c)            #Se  crea una interfaz grafica
	prendido=False          #Variable booleana que permitira la orden de prender o apagar el Led
	btn_led = tkinter.Button(frame, text="Led") #Agrega un boton ala interfaz grafica con el texto Led y ejecutara el metodo Ledonoff cuando se presione el boton
	btn_led.pack()  
