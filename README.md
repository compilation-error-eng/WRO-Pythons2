WRO FUTURE ENGINEERS
The pythons 2

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







