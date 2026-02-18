from machine import Pin
import time
pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

in1 = Pin(14, Pin.OUT)
in2 = Pin(25, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(27, Pin.OUT)

pb1 = Pin(18, Pin.IN, Pin.PULL_UP)
pb2 = Pin(22, Pin.IN, Pin.PULL_UP)  

my_t = 0.002

while True:
    if pb1.value() == 0:
        for k in range(0,500):
            for i in pos:
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                time.sleep(my_t)

    elif pb2.value() == 0:
        for i in range(0,500):
            for i in reversed(pos):
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                time.sleep(my_t)

    else:
        in1.value(0)
        in2.value(0)
        in3.value(0)
        in4.value(0)

