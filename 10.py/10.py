import tkinter
import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO  
from fixed01 import getExample01
from fixed02 import getExample02
from fixed03 import getExample03
from fixed04 import getExample04
from fixed05 import getExample05
from fixed06 import getExample06
from fixed07 import App
from fixed08 import getExample08
root = tkinter.Tk(  )
getExample01(root, 0, 0)
getExample02(root, 0, 1)
getExample03(root, 0, 2)
getExample04(root, 1, 0)
getExample05(root, 1, 1)
getExample06(root, 1, 2)
App(root, 2, 0)
getExample08(root, 2, 1)
root.mainloop(  )
GPIO.cleanup()          # Libera el pin y termina
