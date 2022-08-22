#include<Servo.h>
Servo myservo;
int IN3 = 7;
int IN4 = 8; 
int ENB = 5;
char byteRead = ' ';
void setup() {
  // put your setup code here, to run once:
  Serial.begin(19200);
  myservo.attach(12);
  pinMode(IN3 , OUTPUT);
  pinMode(IN4 ,OUTPUT);
  pinMode(ENB, OUTPUT);
}

void loop() {
    // put your main code here, to run repeatedly:
  if(Serial.available()){
    byteRead = Serial.read();
    Serial.println(byteRead);
    if(byteRead == 'R'){
      right();
      Serial.println("turn right");
    }
    else if(byteRead =='r'){
      right_wall();
      Serial.println("right wall");
    }
    else if(byteRead =='l'){
      left_wall();
      Serial.println("left wall");
    }
    else if (byteRead == 'L'){
      left();
      Serial.println("turn left");
    }
    else if(byteRead == 'F'){
      forward();
      Serial.println("forward");
    }
  }
}
