void right(){
    myservo.write(155);
  digitalWrite(IN3 , HIGH); //IN1 -->HIGH,IN2-->LOW   backwards
  digitalWrite(IN4 , LOW);  //IN1 -->LOW , IN2 -->HIGH forward
  analogWrite(ENB ,255);
}
void left(){
    myservo.write(85);
  digitalWrite(IN3 , HIGH); //IN1 -->HIGH,IN2-->LOW   backwards
  digitalWrite(IN4 , LOW);  //IN1 -->LOW , IN2 -->HIGH forward
  analogWrite(ENB ,255);
}
void forward(){
  myservo.write(110);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB ,255);
}
void left_wall(){
  myservo.write(95);
  digitalWrite(IN3 , HIGH); //IN1 -->HIGH,IN2-->LOW   backwards
  digitalWrite(IN4 , LOW);  //IN1 -->LOW , IN2 -->HIGH forward
  analogWrite(ENB ,255);
}
void right_wall(){
  myservo.write(130);
  digitalWrite(IN3 , HIGH); //IN1 -->HIGH,IN2-->LOW   backwards
  digitalWrite(IN4 , LOW);  //IN1 -->LOW , IN2 -->HIGH forward
  analogWrite(ENB ,255);
} 
