# ====================================================================
# ==============      READ FROM SERIAL PORT     ======================
# ====================================================================
from time import sleep
import serial

Counter = 32

SerialConection = serial.Serial('/dev/tty.usbmodem411', 9600)


while True:
    
    SerialConection.write(str(chr(Counter)).encode())
    print(SerialConection.readline().decode())
    
    Counter = (Counter + 1) % 255 
        