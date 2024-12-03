#include <AccelStepper.h>

// Definer motorpinner
AccelStepper motor_FL = AccelStepper(1, 13, 12);
AccelStepper motor_FR = AccelStepper(1, 11, 10);
AccelStepper motor_BL = AccelStepper(1, 9, 8);
AccelStepper motor_BR = AccelStepper(1, 7, 6);

#define MAX_SPEED 800

void setup() {
  Serial.begin(115200);
  Serial.println("Arduino er klar!");

  motor_FL.setMaxSpeed(MAX_SPEED);
  motor_FR.setMaxSpeed(MAX_SPEED);
  motor_BL.setMaxSpeed(MAX_SPEED);
  motor_BR.setMaxSpeed(MAX_SPEED);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    Serial.println("Mottatt kommando: " + command);

    if (command.startsWith("F")) {
      int speed = command.substring(1).toInt();
      moveForward(speed);
    } else if (command.startsWith("B")) {
      int speed = command.substring(1).toInt();
      moveBackward(speed);
    } else if (command == "S") {
      stopMotors();
    } else if (command == "L360") {
      rotateLeft360();
    } else if (command == "R360") {
      rotateRight360();
    } else {
      Serial.println("Ukjent kommando mottatt: " + command);
    }
  }

  motor_FL.runSpeed();
  motor_FR.runSpeed();
  motor_BL.runSpeed();
  motor_BR.runSpeed();
}

void moveForward(int speed) {
  Serial.println("Beveger fremover med hastighet: " + String(speed));
  motor_FL.setSpeed(speed);
  motor_FR.setSpeed(speed);
  motor_BL.setSpeed(speed);
  motor_BR.setSpeed(speed);
}

void moveBackward(int speed) {
  Serial.println("Beveger bakover med hastighet: " + String(speed));
  motor_FL.setSpeed(-speed);
  motor_FR.setSpeed(-speed);
  motor_BL.setSpeed(-speed);
  motor_BR.setSpeed(-speed);
}

void rotateLeft360() {
  Serial.println("Rotasjon 360 grader til venstre.");
  motor_FL.setSpeed(-MAX_SPEED);
  motor_FR.setSpeed(MAX_SPEED);
  motor_BL.setSpeed(-MAX_SPEED);
  motor_BR.setSpeed(MAX_SPEED);
  delay(1000);  // Juster for nøyaktig rotasjon
  stopMotors();
}

void rotateRight360() {
  Serial.println("Rotasjon 360 grader til høyre.");
  motor_FL.setSpeed(MAX_SPEED);
  motor_FR.setSpeed(-MAX_SPEED);
  motor_BL.setSpeed(MAX_SPEED);
  motor_BR.setSpeed(-MAX_SPEED);
  delay(1000);  // Juster for nøyaktig rotasjon
  stopMotors();
}

void stopMotors() {
  Serial.println("Stopper motorene.");
  motor_FL.setSpeed(0);
  motor_FR.setSpeed(0);
  motor_BL.setSpeed(0);
  motor_BR.setSpeed(0);
}
