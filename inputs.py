from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

""" encontrar F de Final y detener """
def checkscreen(file):
    try:
        f=open(file+".txt", encoding = "utf8")
        fil=f.readlines() 
        if fil[20][74]=='F':
            f.close()
            return 0
        f.close()
    except:
        return 1


""" atajos para presionar teclas """
def pulsarTecla(x):
    keyboard.press(x)
    keyboard.release(x)

def pulsarTeclaDeley(x):
    keyboard.press(x)
    keyboard.release(x)
    time.sleep(1)

def combTeclas(x,y):
    keyboard.press(x)
    keyboard.press(y)
    keyboard.release(y)
    keyboard.release(x)

""" escribe la cadena que le ordenemos """
def escribir(cadena):
    for char in cadena:
        pulsarTecla(char)    
