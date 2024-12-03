#include <AccelStepper.h>

// Definer motorpinner for steg- og retningskontroll
AccelStepper motor_FL = AccelStepper(1, 13, 12);
AccelStepper motor_FR = AccelStepper(1, 11, 10);
AccelStepper motor_BL = AccelStepper(1, 9, 8);
AccelStepper motor_BR = AccelStepper(1, 7, 6);

#define MAX_SPEED 800


void setup() {
  Serial.begin(250000);

  // Sett maksimal hastighet for alle motorer
  motor_FL.setMaxSpeed(MAX_SPEED);
  motor_FR.setMaxSpeed(MAX_SPEED);
  motor_BL.setMaxSpeed(MAX_SPEED);
  motor_BR.setMaxSpeed(MAX_SPEED);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');  // Les kommando fra seriell port
    
    // Sjekk etter kommandoformatet "V[vinkel]S[hastighet]"
    if (command.startsWith("V")) {
      int angle = command.substring(1, command.indexOf("S")).toInt();
      int speed = command.substring(command.indexOf("S") + 1).toInt();
      
      // Beregn hastighet for hvert hjul basert på vinkel og hastighet
      moveOmnidirectional(angle, speed);
    } else if (command == "S") {
      stopMotors();  // Stopp motorene hvis kommandoen er "S"
    } else if (command == "L360") {
      rotateLeft360();  // Roter 360 grader til venstre
    } else if (command == "R360") {
      rotateRight360();  // Roter 360 grader til høyre
    }
  }
  
  motor_FL.runSpeed();
  motor_FR.runSpeed();
  motor_BL.runSpeed();
  motor_BR.runSpeed();
}

void moveOmnidirectional(int angle, int speed) {
  // Omregning fra vinkel til hjulhastigheter basert på Mecanum-hjulformelen
  float radians = angle * PI / 180.0;
  float cosA = cos(radians);
  float sinA = sin(radians);
  
  int fl_speed = speed * (sinA + cosA);  // Front-left wheel
  int fr_speed = speed * (sinA - cosA);  // Front-right wheel
  int bl_speed = speed * (sinA - cosA);  // Back-left wheel
  int br_speed = speed * (sinA + cosA);  // Back-right wheel

  motor_FL.setSpeed(fl_speed);
  motor_FR.setSpeed(fr_speed);
  motor_BL.setSpeed(bl_speed);
  motor_BR.setSpeed(br_speed);
}

void rotateLeft360() {
  motor_FL.setSpeed(-MAX_SPEED / 2);
  motor_FR.setSpeed(-MAX_SPEED / 2);
  motor_BL.setSpeed(-MAX_SPEED / 2);
  motor_BR.setSpeed(-MAX_SPEED / 2);
  delay(100);  // Juster for en hel rotasjon
  stopMotors();
}

void rotateRight360() {
  motor_FL.setSpeed(MAX_SPEED / 2);
  motor_FR.setSpeed(MAX_SPEED / 2);
  motor_BL.setSpeed(MAX_SPEED / 2);
  motor_BR.setSpeed(MAX_SPEED / 2);
  delay(1000);  // Juster for en hel rotasjon
  stopMotors();
}

void stopMotors() {
  motor_FL.setSpeed(0);
  motor_FR.setSpeed(0);
  motor_BL.setSpeed(0);
  motor_BR.setSpeed(0);
}
