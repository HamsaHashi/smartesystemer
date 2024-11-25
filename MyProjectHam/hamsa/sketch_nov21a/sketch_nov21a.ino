#include <AccelStepper.h>

// Definer motorpinner for steg- og retningskontroll
AccelStepper motor_FL = AccelStepper(1, 13, 12);

#define MAX_SPEED 800

void setup() {
  Serial.begin(250000);
  motor_FL.setMaxSpeed(MAX_SPEED);  // Sett maksimal hastighet for motoren
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Les én karakter fra seriell port
    
    switch (command) {
      case 'U':  // Opp-tasten
        motor_FL.setSpeed(MAX_SPEED);
        break;
      case 'D':  // Ned-tasten
        motor_FL.setSpeed(-MAX_SPEED);
        break;
      case 'S':  // Stopp
        motor_FL.setSpeed(0);
        break;
    }
  }
  
  motor_FL.runSpeed();  // Utfør motorbevegelse
}
