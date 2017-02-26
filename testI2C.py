
import smbus
import time
# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def writeBlock(block):
    bus.write_i2c_block_data(address, 0, block)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

def writePort4(port,timeFrame,delay,signal):
    writeBlock([port, timeFrame, delay,signal])

def writePort(port,delay):
    writeBlock(port, 1, delay,1)


while True:
    port = input("Enter port ")

    timeFrame = input("timeFrame ")

    delay = input("Enter time ")

    signal = input("signal ")

    writePort4(port, timeFrame,delay,signal)

    print "RPI Hi Arduino I sent you port ", port
    # sleep one second
    time.sleep(1)

    number = readNumber()
    print "Arduino HeyRPI Ireceived adigit ", number












