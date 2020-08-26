import smbus
import time

# Wired to i2c bus 1 on rapsberry pi
# Wired to i2c bus 8 on jetson xavier
# list devices with: 
#kyle@jetson:~$ sudo i2cdetect -y -r 8
#[sudo] password for kyle: 
#     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
#00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
#10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- -- 
#50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#70: -- -- -- -- 74 -- -- -- 

i2c_channel = 8
i2c_address = 0x44 ## address of sensor set by jumpers

bus = smbus.SMBus(i2c_channel) ## initialize the bus

def readRegister(addr):
    return bus.read_byte_data(i2c_address, addr)

def writeRegister(addr, val):
    return bus.write_byte_data(i2c_address, addr, val)

def read2(addr):
    data = bus.read_i2c_block_data(i2c_address, addr, 2)
    temp = ((data[0] << 8) + data[1]) * 0.0078125
    print("read:", data, "temp C:", "{:.2f}".format(temp))
    return temp

while True:
    read2(0x0)
    time.sleep(1)
