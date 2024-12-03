#include <DynamixelSDK.h>
#include <actuator.h>
#include <stdio.h>

#include <Servo.h> 

#define ADDR_PROFILE_VELOCITY 112  

#define ADDR_TORQUE_ENABLE      64
#define ADDR_GOAL_POSITION      116
#define ADDR_PRESENT_POSITION   132

#define DXL_MOVING_STATUS_THRESHOLD 10    

#define PROTOCOL_VERSION        2.0
#define BAUDRATE                57600

#define DEVICENAME              "COM10 Serial Port (USB)" //windows-riktigPort!!
//#define DEVICENAME              "/dev/cu.usbmodem11201 Serial Port (USB)" //på macbooken

//definer minimum og max posisjon og grader :) 
#define MIN_POS                 0
#define MAX_POS                 4095
#define MIN_DEG                 0
#define MAX_DEG                 360           

#define TORQUE_ENABLE           1
#define TORQUE_DISABLE          0

#define DXL_ID1                     0
#define DXL_ID2                     2
#define DXL_ID3                     3
#define DXL_ID4                     4

#define LEN_GOAL_POSITION           4
#define LEN_PRESENT_POSITION        4

// Funcksjonen konverterer degrees to Dynamixel position
int convertDegreeToPosition(int dxl1_goal_degree, int min_pos, int max_pos, int min_deg, int max_deg) {
    return min_pos + ((dxl1_goal_degree - min_deg) * (max_pos - min_pos) / (max_deg - min_deg));
}


dynamixel::PortHandler *portHandler;
dynamixel::PacketHandler *packetHandler;

void setup() {
    Serial.begin(57600);
    Serial.println("START");

  
    portHandler = dynamixel::PortHandler::getPortHandler(DEVICENAME);
    packetHandler = dynamixel::PacketHandler::getPacketHandler(PROTOCOL_VERSION);
    //INITIALISER PORT OG HANDLER + dobbeltsjekker : 

    if (!portHandler->openPort()) {
        Serial.println("Failed to open the port.");
        return;
    } else {
        Serial.println("Port opened successfully.");
    }

    if (!portHandler->setBaudRate(BAUDRATE)) {
        Serial.println("Failed to set baudrate.");
        return;
    } else {
        Serial.println("Baudrate set successfully.");
    }

    // Enable torque for all 3 servo motors
    Serial.println("Enabling torque for all servos...");
    int ids[] = {DXL_ID1, DXL_ID2, DXL_ID3, DXL_ID4};
    for (int i = 0; i < 4; i++) {
        int torque_result = packetHandler->write1ByteTxRx(portHandler, ids[i], ADDR_TORQUE_ENABLE, TORQUE_ENABLE);
        if (torque_result != COMM_SUCCESS) {
            Serial.print("Torque Enable Error for ID ");
            Serial.println(ids[i]);
        } else {
            Serial.print("Torque enabled for ID ");
            Serial.println(ids[i]);
        }
    }

    // Setter "Profile Velocity"/fra DynamixelWizzard for alle tre motorer
    Serial.println("Setting Profile Velocity for all servos...");
    int velocity = 25;  // Adjust velocity
    for (int i = 0; i < 4; i++) {
        int velocity_result = packetHandler->write4ByteTxRx(portHandler, ids[i], ADDR_PROFILE_VELOCITY, velocity);
        if (velocity_result != COMM_SUCCESS) {
            Serial.print("Error setting Profile Velocity for ID ");
            Serial.println(ids[i]);
        } else {
            Serial.print("Profile Velocity set for ID ");
            Serial.println(ids[i]);
        }
    }

    Serial.println("KEEP GOING GIRL"); //soki motivasjon :)
}




void moveServoToAngle(int id, int degree) {
    Serial.print("Moving servo ID ");
    Serial.print(id);
    Serial.print(" to ");
    Serial.print(degree);
    Serial.println(" degrees.");

    int goal_position = convertDegreeToPosition(degree, MIN_POS, MAX_POS, MIN_DEG, MAX_DEG);

    int comm_result = packetHandler->write4ByteTxRx(portHandler, id, ADDR_GOAL_POSITION, goal_position);
    if (comm_result != COMM_SUCCESS) {
        Serial.print("Error sending goal position for ID ");
        Serial.print(id);
        Serial.print(": ");
        Serial.println(packetHandler->getTxRxResult(comm_result));
    } else {
        Serial.print("Goal position sent successfully for servo ID ");
        Serial.println(id);
    }
}
void stop() {
  Serial.println("Stopping all operations.");
  while (true) {
    
    delay(1000);
  }
}



unsigned long previousMillisDXL3 = 0;
unsigned long previousMillisDXL4 = 0;
const unsigned long intervalDXL3 = 1000;  
const unsigned long intervalDXL4 = 500;   

bool DXL3_movedTo250 = false;  
bool DXL3_movedTo265 = false;  
bool DXL4_movedTo215 = false;  

void loop() {
    unsigned long currentMillis = millis();

    
    Serial.println("Starting servo movements...");
    moveServoToAngle(DXL_ID1, 115);  
    delay(500);  

    moveServoToAngle(DXL_ID2, 130);  
    delay(500);

    moveServoToAngle(DXL_ID3, 265);  
    delay(500);
    moveServoToAngle(DXL_ID4, 215);
    delay(1000);


    if (!DXL4_movedTo215 && currentMillis - previousMillisDXL4 >= intervalDXL4) {
        previousMillisDXL4 = currentMillis;
        moveServoToAngle(DXL_ID4, 250);
        Serial.println("DXL_ID4 moved to 215 degrees.");
        DXL4_movedTo215 = true;
    }
    
    delay(600);  
    Serial.println("Delay of 600 ms executed.");

    // Beveger DXL_ID3 til 250 grader samtidig som DXL_ID4 holder 215 grader; aka for å holde ballen
    if (!DXL3_movedTo250 && currentMillis - previousMillisDXL3 >= intervalDXL3) {
        previousMillisDXL3 = currentMillis;
        moveServoToAngle(DXL_ID3, 170);
        Serial.println("DXL_ID3 moved to 250 degrees.");
        DXL3_movedTo250 = true;
    }

    // Flytter DXL_ID3 tilbake til 265 grader etter at den har nådd 250 grader
    if (DXL3_movedTo250 && !DXL3_movedTo265 && currentMillis - previousMillisDXL3 >= intervalDXL3 + 1000) {
        previousMillisDXL3 = currentMillis;
        moveServoToAngle(DXL_ID3, 265);
        Serial.println("DXL_ID3 moved back to 265 degrees.");
        DXL3_movedTo265 = true;
    }

    // Flytt DXL_ID4 til 250 grader etter at DXL_ID3 er flyttet tilbake til 265 grader
    if (DXL3_movedTo265 && currentMillis - previousMillisDXL4 >= intervalDXL4 + 1500) {
        moveServoToAngle(DXL_ID4, 215);
        Serial.println("DXL_ID4 moved to 250 degrees.");
        delay(500); // Litt forsinkelse før loopen starter på nytt
        DXL4_movedTo215 = false;
        DXL3_movedTo250 = false;
        DXL3_movedTo265 = false;
    }


    moveServoToAngle(DXL_ID3, 180);
    delay(500);

    moveServoToAngle(DXL_ID2, 180);
    delay(500);

    moveServoToAngle(DXL_ID1, 88);
    delay(500); 

  

    //plassere ballen i en av kurvene: 
    moveServoToAngle(DXL_ID1, 151);
    delay(500);

    moveServoToAngle(DXL_ID2, 280);
    delay(500);

    moveServoToAngle(DXL_ID3, 90);
    delay(500);

    moveServoToAngle(DXL_ID4, 215);
    delay(500);

    //moveServoToAngle(DXL_ID4, 255);
    //delay(1000);

    

    // Leser+skriv nåværende posisjon for alle servoer
    Serial.println("Reading current positions of all servos...");
    int ids[] = {DXL_ID1, DXL_ID2, DXL_ID3, DXL_ID4};
    for (int i = 0; i < 4; i++) {
        int present_position;
        uint8_t dxl_error;
        int result = packetHandler->read4ByteTxRx(portHandler, ids[i], ADDR_PRESENT_POSITION, (uint32_t *)&present_position, &dxl_error);

        if (result != COMM_SUCCESS) {
            Serial.print("Read Error for ID ");
            Serial.print(ids[i]);
            Serial.print(": ");
            Serial.println(packetHandler->getTxRxResult(result));
        } else if (dxl_error != 0) {
            Serial.print("Dynamixel Error for ID ");
            Serial.print(ids[i]);
            Serial.print(": ");
            Serial.println(dxl_error, HEX);
        } else {
            Serial.print("Servo ID ");
            Serial.print(ids[i]);
            Serial.print(" Present Position: ");
            Serial.println(present_position);
        }
    }

    
    Serial.println("Waiting before restarting the loop...");
    delay(1000);
    //brukes kun for videoen 
    stop();

}

