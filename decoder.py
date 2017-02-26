

GET_STATE = 2
SET_1 = 1
SET_0 = 0

def decode(port,command):
    value=(command<<4)+port
    print value
    return value
print decode(1,GET_STATE)
