import time
import serial 
import keybord as KB
transmitter = serial.Serial('COM10', 115200, timeout=10000)
transmitter.write("1".encode('utf-8'))
PW=50
ST=0.5
w= (PW/100)*ST
s= ST - w
def forward(): 
    global TExt
    transmitter.write("F".encode('utf-8'))
    TExt="F"

def back():
    global TExt
    transmitter.write("B".encode('utf-8'))
    TExt="B"

def stop():
    global TExt
    transmitter.write("S".encode('utf-8'))
    TExt="S"

def rotc():
    global TExt
    transmitter.write("X".encode('utf-8'))
    TExt="X"

def rotcc():
    global TExt
    transmitter.write("Z".encode('utf-8'))
    TExt="Z"

def left():
    global TExt
    transmitter.write("L".encode('utf-8'))
    TExt="L"

def right():
    global TExt
    transmitter.write("R".encode('utf-8'))
    TExt="R"

def pforward(): 
    forward()
    time.sleep(w)
    stop()
    time.sleep(s)

def pback():
    back()
    time.sleep(w)
    stop()
    time.sleep(s)

def protc():
    rotc()
    time.sleep(w)
    stop()
    time.sleep(s)

def protcc():
    rotcc()
    time.sleep(w)
    stop()
    time.sleep(s)

def pleft():
    left()
    time.sleep(w)
    stop()
    time.sleep(s)

def pright():
    right()
    time.sleep(w)
    stop()
    time.sleep(s)


while True:
    if KB.is_pressed('w'):
        pforward()
    elif KB.is_pressed('q'):
        protc()
    elif KB.is_pressed('s'):
        pback()
    else:
        stop()

