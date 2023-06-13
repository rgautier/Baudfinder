import serial
from time import sleep

baud_dict = [2400, 4800, 9600, 14400, 19200, 2800, 38400, 57600, 76800, 115200, 230400]

for baud_rate in baud_dict:
    print("Trying baud rate of: " + str(baud_rate))
    ser = serial.Serial('COM6', baud_rate, timeout=1)
    print(ser)
    line = ser.read(100)
    sleep(3)
    ser.close()
    print(line)
    sleep(5)