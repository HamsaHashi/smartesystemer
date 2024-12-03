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

#define DEVICENAME              "COM10 Serial Port (USB)"
//#define DEVICENAME              "/dev/cu.usbmodem11201 Serial Port (USB)"

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

// Function to convert degrees to Dynamixel position
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

    // Enable torque for all three servo motors
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

    // Set Profile Velocity for all three motors
    Serial.println("Setting Profile Velocity for all servos...");
    int velocity = 45;  // Adjust velocity
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





    Serial.println("KEEP GOING GIRL");
    //så langt kjærer alt bra!

    //packetHandler->write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE);
    //Serial.println("AFTER X");
    
    //int dxl1_goal_position = convertDegreeToPosition(DXL1_GOAL_DEGREE, MIN_POS, MAX_POS, MIN_DEG, MAX_DEG);
    //Serial.println("Calculated Goal Position: "); 
    //Serial.println(dxl1_goal_position);
    //packetHandler->write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, dxl1_goal_position);
    //Serial.println("KEEP GOING GIRL");
    //int goal_position = 2048;
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


unsigned long previousMillisDXL3 = 0;
unsigned long previousMillisDXL4 = 0;
const unsigned long intervalDXL3 = 1000;  // Forsinkelse for DXL3
const unsigned long intervalDXL4 = 500;   // Forsinkelse for DXL4

bool DXL3_movedTo250 = false;  // For å sjekke om DXL3 er flyttet til 250 grader
bool DXL3_movedTo265 = false;  // For å sjekke om DXL3 er flyttet tilbake til 265 grader
bool DXL4_movedTo215 = false;  // For å sjekke om DXL4 er flyttet til 215 grader

void loop() {
    unsigned long currentMillis = millis();

    // Move all three servos to their respective angles
    Serial.println("Starting servo movements...");
    moveServoToAngle(DXL_ID1, 115);  // Move servo ID 0 to 150 degrees
    delay(500);  // Delay for synchronization

    moveServoToAngle(DXL_ID2, 130);  // Move servo ID 2 to 135 degrees
    delay(500);

    moveServoToAngle(DXL_ID3, 265);  // Move servo ID 3 to 100 degrees
    delay(500);
    moveServoToAngle(DXL_ID4, 215);
    delay(1000);

    // Beveg DXL_ID4 til 215 grader
    if (!DXL4_movedTo215 && currentMillis - previousMillisDXL4 >= intervalDXL4) {
        previousMillisDXL4 = currentMillis;
        moveServoToAngle(DXL_ID4, 250);
        Serial.println("DXL_ID4 moved to 215 degrees.");
        DXL4_movedTo215 = true;
    }
    // Legg til delay(600) her
    delay(600);  // Forsinkelse på 600 ms
    Serial.println("Delay of 600 ms executed.");

    // Beveg DXL_ID3 til 250 grader samtidig som DXL_ID4 holder 215 grader
    if (!DXL3_movedTo250 && currentMillis - previousMillisDXL3 >= intervalDXL3) {
        previousMillisDXL3 = currentMillis;
        moveServoToAngle(DXL_ID3, 170);
        Serial.println("DXL_ID3 moved to 250 degrees.");
        DXL3_movedTo250 = true;
    }

    // Flytt DXL_ID3 tilbake til 265 grader etter at den har nådd 250 grader
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

    // Les og skriv nåværende posisjon for alle servoer
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

    // Delay før neste iterasjon
    Serial.println("Waiting before restarting the loop...");
    delay(1000);
}

