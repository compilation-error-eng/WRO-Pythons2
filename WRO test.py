# Untitled - By: pc - Wed Jul 20 2022

import sensor, image, time, pyb
from pyb import UART
led = pyb.LED(3)
thresholds1 = [(33, 53, -128, -12, 9, 124)] #green threshold
thresholds2 = [(22, 58, 10, 127, -2, 34)] #red threshold
EXPOSURE_TIME_SCALE =2
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_vflip(True)
sensor.set_hmirror(True)
current_exposure_time_in_microsecond  = sensor.get_exposure_us()
clock = time.clock()
#sensor.set_auto_exposure(False,  exposure_us=int(current_exposure_time_in_microsecond * EXPOSURE_TIME_SCALE))
sensor.set_auto_exposure(False,15000)
uart = UART(1, 19200)
greenflag = False
redflag = False
while(True):
    led.on()
    clock.tick()
    led.off()
    img = sensor.snapshot()
    print(clock.fps())
    greenblob = img.find_blobs(thresholds1,pixel_threshld=500, area_threshold=3000,merge=True)
    if greenblob:
        img.draw_rectangle(greenblob[0].rect(),color=(0,255,0))
        img.draw_cross(greenblob[0].cx(),greenblob[0].cy())
        print("turn left")
        uart.write('L')
        print("area of greenblob",greenblob[0].area())
        greenflag = True
    else:
        greenflag = False
    redblob = img.find_blobs(thresholds2,pixel_threshld=500, area_threshold=3000,merge=True)
    if redblob :
        img.draw_rectangle(redblob[0].rect(),color=(255,0,0))
        img.draw_cross(redblob[0].cx(),redblob[0].cy())
        print("turn right")
        uart.write('R')
        print("area of redblob",redblob[0].area())
        redflag = True
    else:
        redflag = False

    if greenflag == False and redflag== False:
        print("no green no red , forward")
        uart.write('F')
