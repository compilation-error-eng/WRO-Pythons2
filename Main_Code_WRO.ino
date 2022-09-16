#include<Servo.h>
Servo myservo;
int IN3 = 7;
int IN4= 8;
int i=0;
int ENB = 5;
bool flag = true;
int yaw;
int yaw_initial;
char byteRead = ' ';
bool LR=false;
void setup() {
  
    Serial.begin(115200);
    myservo.attach(12);
    pinMode(IN3 , OUTPUT);
    pinMode(IN4 ,OUTPUT);
    pinMode(ENB , OUTPUT);
    imu_setups();
}

void loop() {
      yaw =imu_loop();
      //Serial.println(yaw);
       if(Serial.available()){
         //Serial.println("work");
            byteRead = Serial.read();
            //Serial.println(byteRead);
            if(flag == false){
              digitalWrite(13, HIGH);
             if(i<45){
            if(LR == false) right();
            else left();
              
             // Serial.println("going right");
              if (yaw != yaw_initial) {
                yaw_initial = yaw;
                i ++;
                //Serial.println(i);
              }
            }
            else{
               
                stops();
                flag=true;
                i=0; 
                //Serial.println("stop");
            }
            if (byteRead == 'R' || byteRead == 'L' ){
              flag = true;
              i=0;
            }
          }
          else{
            digitalWrite(13, LOW);
            if(byteRead == 'B'){
                  if(flag){
                  yaw_initial = yaw;
                  flag = false;
                  LR=true;
                  }
            }
            else if(byteRead == 'O'){
               if(flag ){
              //digitalWrite(13, HIGH);
              yaw_initial = yaw;
              flag = false;
              LR=false;
              }
            
            else if(byteRead == 'R'){
                  right();
                  //Serial.println("turn right");
                  flag=true;
            }
            
            }
            else if(byteRead =='r'){
              right_wall();
              //Serial.println("right wall");
              
            }
            else if(byteRead == 'S'){
              stops();
            }
            else if(byteRead =='l'){
              left_wall();
              //Serial.println("left wall");
              
            }
            else if (byteRead == 'L'){
              left();
              //Serial.println("turn left");
              flag=true;
            }
            else if(byteRead == 'F'){
              forward();
              //Serial.println("forward");
            }
            else if (byteRead == 'b'){
              backwards();
              delay(100);
            }
      }
          }

}
//-88  -1 --->1
