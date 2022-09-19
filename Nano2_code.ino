#include <SoftwareSerial.h>

SoftwareSerial mySerial(7, 8); // RX, TX
int yaw;
int yaw_initial;
void setup()
{
  // Open serial communications and wait for port to open:
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Native USB only
  }
  mySerial.begin(38400);
  imu_setups();
 
}

void loop() // run over and over
{
   yaw =imu_loop();
   Serial.println(yaw);
   mySerial.println(yaw);
}
