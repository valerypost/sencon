
import time

# for RPI version 1, use bus = smbus.SMBus(0)
# bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    # bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def writeBlock(block):
    # bus.write_i2c_block_data(address, 0, block)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    # number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return 1

def writePort4(port,timeFrame,delay,signal):
    writeBlock([port, timeFrame, delay,signal])

def writePort(port,delay):
    writeBlock(port, 1, delay,1)



def write(port,command):
    value=decoder.decode(port,command)
    writeNumber(value)
    print "write value",value
    return -1

def request(port):
    writeBlock([port, 10, 1, 0])
    time.sleep(1)
    number = readNumber()
    return number


def getPower():
    value= request(7)
    if value == 1 :
        return "checked"
    else:
        return ""


def setPower(time):
    writePort4(7, 1, time, 1)

