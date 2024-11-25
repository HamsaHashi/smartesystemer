#include "kinematics.h"
#include "matrixUtils.h"


#define NUM_JOINTS 3 //antall ledd nb. ikke inkl grepet aka DXL4 

void setup() {
    Serial.begin(9600);

    Kinematics kin(NUM_JOINTS);
    MatrixUtils mat_utils;

    kin.add_joint_axis(0, 0, 1);  // Joint 1 konfigurasjon
    kin.add_joint_axis(0, 0, 0);  // Joint 2 konfigurasjon
    kin.add_joint_axis(0, 0, -1); // Joint 3 konfigurasjon
/Users/sokainacherkane/Documents/Arduino/libraries/Kinematics/examples/inverse_kinematics/inverse_kinematics.ino
   
    kin.add_initial_end_effector_pose(-1, 0, 0,
                                       0, 1, 0,
                                       0, 0, 1);

    
    float joint_angles[NUM_JOINTS] = {PI / 2.0, 3.0, PI};
    float transform[3][3];

    
    kin.forward(joint_angles, (float*)transform);
    
    
    mat_utils.print_matrix((float*)transform, 3, 3, "Transform");

    
}

void loop() {
    // koden kjøres repeatedly, men i dette tilfelle (forwardKin) trenger vi kun void setup()

}
