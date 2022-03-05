#This program runs in the background and reads the latest broadband speed and sends it to the 
#Raspberry Pi Pico.
#

import time
import serial
import speedtest
import sys

ser = None

if len(sys.argv) == 1:
    print("No arguements - initializing serial")
    ser = serial.Serial(
        port = '/dev/ttyACM0', 
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
else:
    print("Not initializing serial")

st = speedtest.Speedtest()

msg = ""
i = 0

#Initialize Dial by sending a 0
#Make sure to end the line of everything you send! '\n'
init_val = "0\n"
if ser:
    ser.write(init_val.encode('utf-8'))

max_speed = 0.00
min_speed = 2000.00

max_out = 6000
min_out = 500

num_sample = 0

while True:
    print("Getting download speed...")
    download_speed = st.download() / 1048576
    num_sample += 1
    print("Current Download Speed: {} Mbit/s".format(download_speed))
    if download_speed > max_speed: 
        max_speed = download_speed
    if download_speed < min_speed:
        min_speed = download_speed

    #Scale current download speed based on min/max speeds
    #Current Scale: 500 - Min, 6000 - Max
    if num_sample < 5: 
        adjusted_val = (max_out - min_out)/2
    else:
        adjusted_val = ((max_out - min_out)/(max_speed - min_speed))*(download_speed - min_speed) + min_out

    output_val = str((int(adjusted_val))) + "\n"
    if ser:
        print("Encoding: {} Mbit/s".format(str(int(adjusted_val))))
        ser.write(output_val.encode('utf-8'))
    time.sleep(60)

