# Untitled - By: pc - Wed Jul 20 2022

import sensor, image, time, pyb
from pyb import UART
led = pyb.LED(2)
led2 = pyb.LED(3)
threshold1 = [(24, 40, -128, -15, 2, 127)] #green threshold
threshold2 = [(0, 45, 28, 127, -1, 127)] #red threshold
thresholds = [(0, 21, -128, 127, -128, 127)] #wall threshold
threshold_LB = [(19, 50, -1, 19, -128, -23)]#blue line threshold
threshold_LO = [(41, 53, 18, 127, -128, 127)]#orange line threshold
ROIl = [ (20, 60, 120, 90, 0.7)]#left roi of wall
ROIR = [(200, 60, 120, 90, 0.7)] #right roi of wall
ROIL = [ (20, 180, 320, 40, 0.7)] # blue orange line roi
EXPOSURE_TIME_SCALE =2
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.set_auto_exposure(False,15000)
#sensor.set_brightness(1)

#current_exposure_time_in_microsecond  = sensor.get_exposure_us()
clock = time.clock()
#sensor.set_auto_exposure(False,  exposure_us=int(current_exposure_time_in_microsecond * EXPOSURE_TIME_SCALE))
#sensor.set_auto_exposure(False,15000)
uart = UART(1, 19200)
greenflag = False
redflag = False
wall_flag = False
orange_flag = False
blue_flag = False
while(True):
    clock.tick()
    img = sensor.snapshot()
    #print(clock.fps())
    for r in ROI:
            orange_lines = img.find_blobs(thresholds,roi=r[0:4], pixelthreshold=500, areathreshold=1000)
            blue_lines = img.find_blobs(thresholds2, roi=r[0:4], pixelthreshold=500, areathreshold=1000)

            if orange_lines and blue_flag = False:
                print(orange_lines[0].area())
                img.draw_rectangle(orange_lines[0].rect())
                img.draw_cross(orange_lines[0].cx(),orange_lines[0].cy())
                print("orange line found going right")
                uart.write("r")
                orange_flag = True
                line_flag = True
            elif blue_lines and orange_flag=False:
                img.draw_rectangle(blue_lines[0].rect())
                img.draw_cross(blue_lines[0].cx(),blue_lines[0].cy())
                print("blue light found turning left")
                uart.write("l")
                blue_flag = True
                line_flag = True
            else:
                line_flag = False
    if line_flag == False:
        greenblob = img.find_blobs(threshold1,pixel_threshld=500, area_threshold=2000,merge=True)
        if greenblob:
                img.draw_rectangle(greenblob[0].rect(),color=(0,255,0))
                img.draw_cross(greenblob[0].cx(),greenblob[0].cy())
                print("turn left")
                uart.write('L')
                time.sleep(0.1)
                print("area of greenblob",greenblob[0].area())
                greenflag = True

        else:
                greenflag = False
                print("no green")
        redblob = img.find_blobs(threshold2,pixel_threshld=500, area_threshold=1000,merge=True)

        if redblob :
                redflag = True
                img.draw_rectangle(redblob[0].rect(),color=(255,0,0))
                img.draw_cross(redblob[0].cx(),redblob[0].cy())
                print("turn right red")
                uart.write('R')
                time.sleep(0.1)
                print("area of redblob",redblob[0].area())

        else:
                redflag = False
                print("no red")

        if redflag == False and greenflag == False:
            wall_flag = True
        else:
            wall_flag = False
        if wall_flag == True:
            for l in ROIl:
                left_wall = img.find_blobs(thresholds,roi=l[0:4],pixelthreshold=100, areathreshold=500,merge=True)
                if left_wall:
                    area_leftwall = left_wall[0].area()
                    img.draw_rectangle(left_wall[0].rect())
                    img.draw_cross(left_wall[0].cx(), left_wall[0].cy())

            for r in ROIR :
                right_wall = img.find_blobs(thresholds ,roi=r[0:4], pixelthreshold=100, areathreshold=500, merge=True)
                if right_wall:
                    area_rightwall = right_wall[0].area()
                    img.draw_rectangle(right_wall[0].rect())
                    img.draw_cross(right_wall[0].cx(), right_wall[0].cy())

            wall_diff = area_rightwall-area_leftwall
            print(wall_diff)
            if wall_diff >=900:
                print("turn left wall")
                uart.write("l")
            elif wall_diff <= -20:
                print("turn right wall")
                uart.write("r")
            elif 900>wall_diff>-20:
                print("forward wall")
                uart.write("F")
