from machine import Pin, PWM
import utime

dial = Pin(17, Pin.OUT)
dial_pwm = PWM(dial)
dial_pwm.freq(1000)

dial_pwm.duty_u16(9300)
#Milliamperes on pin 
#3000 - 0
#4000 - .2
#5000 - .32
#6000 - .38
#7000 - .6
#8000 - .77
#9000 - .94
#9300 - 1.0


while True:
    for i in range(1000, 6000):
        dial_pwm.duty_u16(i)
        utime.sleep_us(2000)
