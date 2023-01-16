from machine import UART, Pin
import time
import json

uart1 = UART(0, baudrate = 38400, tx= Pin(0), rx=Pin(1))
str2 = "lo"

while (True):
    uart1.write('salut')
    print(uart1.read(5))
    if uart1.any() > 0:
        strBT = str(uart1.readline(),"utf-8")
        print(strBT)
        strSplit = strBT.split(";")
        print(strSplit[0])
        for x in range(len(strSplit)):
            print(strSplit[x])
    time.sleep(1)