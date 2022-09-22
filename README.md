<u> WRO FUTURE ENGINEERS
The pythons 2 <u>

This is a detailed documentation of our project in the WRO FUTURE ENGINEERS competition of my team that consist of 3 people and our coach Omar Khaled Elsayed . My name is Ahmed Elsayed and I am responsible for the programming of the robot , my teammates are Nour Raoof and Eyad Ahmed Nazary each are responsible for the mechanical and the electrical section of the robot respectively . We are from Egypt and are joining the WRO competition for the first time and I am going to explain the steps and procedures that went into creating our robot.

Firstly: Our components
For seeing the blocks and moving accordingly we used the Openmv H7 plus camera module it is a cheap easy to buy camera module that is similar to the raspberry pi but is much cheaper here is a photo of it:
![openmv1](https://user-images.githubusercontent.com/53234566/190664656-b2dc7a8f-ef66-465b-81c5-f77d46647ddd.jpg)
Link of component can be found at the end


For communicating with the camera module we used and the motors to move accordingly we used an ordinary Arduino Nano 
A photo of it:
![index](https://user-images.githubusercontent.com/53234566/190664654-73a4b632-6b9f-42ce-ab9c-55d61f8951d9.jpg)

Link can be found later



We used the l298 motor driver to move the motor forward and backwards and it is small and suitable for one motor which is required
![f636e246-1f8f-4bf6-931c-e3b472912639 __CR00970600_PT0_SX970_V1___](https://user-images.githubusercontent.com/53234566/190664635-2c49e76e-5c60-420d-9378-1c031fe2292c.jpg)





For the battery we used a normal 12volt battery with 3600mah

For our steering mechanism we used a servo motor connected to a rod that controls the position of the robot.



![YM2758-arduino-compatible-9g-micro-servo-motorImageMain-515](https://user-images.githubusercontent.com/53234566/190664667-5a128ea8-c32c-4e85-afb5-55801c2c1afe.jpg) 


We also used an IMU sensor to control the deviation of the robot from its origin point in certain turns 


![imu sensor](https://user-images.githubusercontent.com/53234566/190664649-3865e52b-9e65-4574-ab5f-0e2042d5aea7.jpg) 


We used a stepdown buck converter DC to DC to convert the 12volts that are coming from the battery to 9 volts in order for the Arduino Nano to use it


![buck convertor](https://user-images.githubusercontent.com/53234566/190664628-ebff8b66-d8b5-4184-9526-bde0ec09e846.jpg)


Links:

Arduino Nano:
https://store.arduino.cc/products/arduino-nano

l298 motordriver:
https://store.fut-electronics.com/products/l298-dual-motor-driver-module-2a

IMU sensor:
https://makerselectronics.com/product/imu-mpu-6050-gyroscope-accelerometer-sensor-module

buck cnovertor:
https://makerselectronics.com/product/xl4015-step-down-dc-module-with-cv-cc-control

servo motor:
https://makerselectronics.com/product/micro-servo-sg92r

openmv H7 R2 camera:
https://openmv.io/products/openmv-cam-h7-r2
 

Explenation for the code:

we divided the code into steps :
1. Blocks
2. lines
3. walls
ordered according to priority

I will now explain each step briefly:

1. Blocks:
we used a simple searching algorithm where the camera search in aspecified ROI (Region Of Intrest)
and applied a threshold for the camera to see only the specified color which is either Green or Blue we also used this for the rest of the algorithm
but in the code it is important to make the blocks the highest priority so it can turn around it even if there is a line

2. Lines:
In the lines it was a little diffrent from the blocks because u have two lines with diffrent colours and u need to turn according to the forst one the camera sees and u can simply do that with flags and counters make a counter that starts counting when it sees orange (or blue if u started on the oppisite)
then if that counter gets high enough that means that he needs to turn the next time he sees a line otherwise dont turn and we also used the IMU MPU sensor to calculate degree of turn and made him turn only 45 degrees so he turns according to the block if there is one

3. Walls:
in the walls it was pretty simple but because of my camera was a little bugged it only saw one wall ond rarely sees the two lines togethor so i modified the 
original algorithm to suite my bugged camera which is always easier than getting a new camera i made 3 cinditions in total if the robot sees only the right wall it will position itself according to it , if it sees only the left wall it will also posistion itself accordingly  and if it sees the 2 walls togethor
(which rarely happens) this algorithm works but ofcourse it does have its bugs but i cant really afford a new camera so im sticking with this until i afford it

electric schematic of the robot:

![WRO schematic](https://user-images.githubusercontent.com/53234566/191744019-a79c87a5-899a-4dea-8a62-5bf5a44dc9ad.png)


pictures of robot:

Front view:
![20220922_151222](https://user-images.githubusercontent.com/53234566/191758058-3cbd28ec-5724-4a01-979f-55adad4fea03.jpg)

left view:
![20220922_151230](https://user-images.githubusercontent.com/53234566/191758571-ab9573af-a859-4f47-8eb2-d29ef0bdb196.jpg)

Back view:
![20220922_151238](https://user-images.githubusercontent.com/53234566/191759400-ccd105cb-362a-457c-8fb2-9538c3bfe891.jpg)

Right view:
![20220922_151214](https://user-images.githubusercontent.com/53234566/191759758-44a14a42-e6a3-4a12-971a-a43b15dc9b1d.jpg)

Top view:
![20220922_151308](https://user-images.githubusercontent.com/53234566/191760222-13e0ce86-7adc-4e3d-9656-cb318bbffb24.jpg)

Bottom view:
![20220922_151442](https://user-images.githubusercontent.com/53234566/191760910-aeb3f4a3-2be7-41a6-9fe4-b565a072f535.jpg)

