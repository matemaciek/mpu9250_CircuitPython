import board, busio, mpu9250, time

i2c = busio.I2C(board.GP27, board.GP26)
imu = mpu9250.IMU(i2c)
while(True):
    print(imu.acc, "g")
    print(imu.gyr, "º/s")
    print(imu.mag, "uT")
    print(imu.tmp, "ºC")
    time.sleep(0.5)
