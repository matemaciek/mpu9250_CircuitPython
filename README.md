# mpu9250_CircuitPython
Simple MPU9250 over I2C client working with CircuitPython.

Developed for CP v6.2.

Don't need any extra libraries.

Heavilly inspired by:
- https://github.com/makerportal/mpu92-calibration/blob/main/mpu9250_i2c.py
- https://github.com/wallarug/CircuitPython_MPU9250/blob/master/hybrid/roboticsmasters_mpu9250.py

## Example
Copy `mpu9250.py` to `/lib` folder on your board and run code below (`example.py`): 
```
import board, busio, mpu9250, time

i2c = busio.I2C(board.GP27, board.GP26)
imu = mpu9250.IMU(i2c)
while(True):
    print(imu.acc, "g")
    print(imu.gyr, "º/s")
    print(imu.mag, "uT")
    print(imu.tmp, "ºC")
    time.sleep(0.5)
```
