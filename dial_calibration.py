#This program takes an input value and outputs that on the serial line
#Raspberry Pi Pico.
#

import time
import serial
import speedtest
import sys

ser = None

max_speed = 0.00
min_speed = 2000.00

max_out = 6000
min_out = 500

num_sample = 0

if len(sys.argv) == 1:
    print("No arguements - initializing default unix serial")
    ser = serial.Serial(
        port='/dev/ttyACM0', 
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
elif len(sys.argv) == 2:
    user_port=sys.argv[1]
    print("Initialzing with device on port {}".format(user_port))
    ser = serial.Serial(
        port=user_port,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
else:
    print("Not initializing serial")
    print("Usage: broadband_sender.py [COM PORT] [MIN OUTPUT, MAX OUTPUT]")

msg = ""
i = 0

#Initialize Dial by sending a 0
#Make sure to end the line of everything you send! '\n'
init_val = "0\n"
if ser:
    ser.write(init_val.encode('utf-8'))
    
real_min = 0
real_max = 1000

while True:

    adjusted_val = input("Enter encoder value: ")

    output_val = str((int(adjusted_val))) + "\n"
    if ser:
        print("Encoding: {} Mbit/s".format(str(int(adjusted_val))))
        ser.write(output_val.encode('utf-8'))
