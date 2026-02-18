from machine import Pin
import time

pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

in1 = Pin(14, Pin.OUT)
in2 = Pin(25, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(27, Pin.OUT)

my_t = 0.005

while True:
    for k in range(0,500):
        for i in (pos):
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep(my_t)
            
    for k in range(0,500):
        for i in reversed(pos):
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep(my_t)
