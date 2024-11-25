#include <AccelStepper.h>

// Definer motorpinner
AccelStepper motor_FL = AccelStepper(1, 13, 12); // Front-left
AccelStepper motor_FR = AccelStepper(1, 11, 10); // Front-right
AccelStepper motor_BL = AccelStepper(1, 9, 8);   // Back-left
AccelStepper motor_BR = AccelStepper(1, 7, 6);   // Back-right

#define MAX_SPEED 500  // Maksimal hastighet for motorene
#define TIMEOUT 300    // Timeout i millisekunder for automatisk stopp

unsigned long lastCommandTime = 0;  // Tidspunkt for siste kommando

void setup() {
  Serial.begin(115200);
  Serial.println("Arduino er klar!");

  // Sett maksimal hastighet for alle motorer
  motor_FL.setMaxSpeed(MAX_SPEED);
  motor_FR.setMaxSpeed(MAX_SPEED); 
  motor_BL.setMaxSpeed(MAX_SPEED);
  motor_BR.setMaxSpeed(MAX_SPEED);
  motor_FL.setAcceleration(200 );  // Eksempel: Sett en moderat akselerasjon
  motor_FR.setAcceleration(200);
  motor_BL.setAcceleration(200);
  motor_BR.setAcceleration(200);

}

void loop() {
  // Sjekk om det har kommet nye kommandoer
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    Serial.println("Mottatt kommando: " + command);

    if (command.startsWith("V")) {
      int angle = command.substring(1, command.indexOf("S")).toInt();
      int speed = command.substring(command.indexOf("S") + 1).toInt();
      moveOmnidirectional(angle, speed);
    } else if (command == "S") {
      stopMotors();
    } else {
      Serial.println("Ukjent kommando mottatt: " + command);
    }

    // Oppdater tidspunkt for siste gyldige kommando
    lastCommandTime = millis();
  }

  // Timeout: Stopp motorene hvis ingen kommando mottas innenfor tidsrammen
  if (millis() - lastCommandTime > TIMEOUT) {
    stopMotors();
  }

  // Oppdater motorene kontinuerlig
  motor_FL.runSpeed();
  motor_FR.runSpeed();
  motor_BL.runSpeed();
  motor_BR.runSpeed();
}

void moveOmnidirectional(int angle, int speed) {
  // Konverter vinkel fra grader til radianer
  float radians = angle * PI / 180.0;
  float cosA = cos(radians);
  float sinA = sin(radians);

  // Beregn hjulhastigheter basert på Mecanum-hjulformelen
  int fl_speed = speed * (sinA + cosA);  // Front-left wheel
  int fr_speed = speed * (sinA - cosA);  // Front-right wheel
  int bl_speed = speed * (sinA - cosA);  // Back-left wheel
  int br_speed = speed * (sinA + cosA);  // Back-right wheel

  // Debugging: Print hjulhastigheter
  Serial.print("Hjulhastigheter: ");
  Serial.print("FL: "); Serial.print(fl_speed);
  Serial.print(", FR: "); Serial.print(fr_speed);
  Serial.print(", BL: "); Serial.print(bl_speed);
  Serial.print(", BR: "); Serial.println(br_speed);

  // Sett hastighet for hvert hjul
  motor_FL.setSpeed(fl_speed);
  motor_FR.setSpeed(fr_speed);
  motor_BL.setSpeed(bl_speed);
  motor_BR.setSpeed(br_speed);
}

void stopMotors() {
  // Sett alle motorer til null hastighet
  motor_FL.setSpeed(0);
  motor_FR.setSpeed(0);
  motor_BL.setSpeed(0);
  motor_BR.setSpeed(0);
  Serial.println("Motorene er stoppet.");
}
