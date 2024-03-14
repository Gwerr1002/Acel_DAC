from MCP4725 import MCP4725,I2C
from machine import Pin
from IMU import MPU6050

def main():
    i2c = I2C(1,sda=Pin(21), scl=Pin(22), freq=400000)
    dac = MCP4725(i2c,96,5)
    dac.config()
    imu = MPU6050(i2c,0)
    imu.accel_range=1
    m = 27.71
    while(True):
        i = (((imu.accel.x+4)**2+(imu.accel.y+4)**2+(imu.accel.z+4)**2))**(1/2)/3
        #print(i)
        dac.setVoltaje(i)
    #return dac

if __name__ == '__main__':
    dac = main()