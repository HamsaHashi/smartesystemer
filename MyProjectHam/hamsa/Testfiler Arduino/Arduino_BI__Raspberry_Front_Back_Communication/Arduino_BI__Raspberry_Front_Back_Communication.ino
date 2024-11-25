#include "Stepper.h"

const int FL_step = 6;
const int FL_dir = 7;
const int FR_step = 8;
const int FR_dir = 9;
const int BL_step = 10;
const int BL_dir = 11;
const int BR_step = 12;
const int BR_dir = 13;

int stepsPerRevolution = 200;

int counter = 0;

void setup() {
  Serial.begin(115200);
  pinMode(FL_step, OUTPUT);
  pinMode(FL_dir, OUTPUT);
  pinMode(FR_step, OUTPUT);
  pinMode(FR_dir, OUTPUT);
  pinMode(BL_step, OUTPUT);
  pinMode(BL_dir, OUTPUT);
  pinMode(BR_step, OUTPUT);
  pinMode(BR_dir, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');
    message = message + " " + String(counter);
    counter++;
    Serial.println(message);
  }
  forward();
}

void forward() {
  digitalWrite(FL_dir, LOW);
  for (int i = 0; i < stepsPerRevolution; i++) {
    digitalWrite(FL_step, HIGH);
    delayMicroseconds(250);
    digitalWrite(FL_step, LOW);
    delayMicroseconds(250);
  }
}
