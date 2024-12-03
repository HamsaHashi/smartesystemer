#ifndef KINEMATICS1_H
#define KINEMATICS1_H

#include <Arduino.h>
#include "MatrixUtils1.h"

class Kinematics {
private:
    int antall_ledd;
    int antall_ledd_deklarert;
    float joint_screw_axes[3][3];
    float initial_end_effector_pose[3][3];
    MatrixUtils mat_utils;

public:
    Kinematics(int antall_Ledd);

    void add_joint_axis(float s1, float s2, float s3);
    void add_initial_end_effector_pose(float m11, float m12, float m13, 
                                        float m21, float m22, float m23, 
                                        float m31, float m32, float m33);
    void forward(float* ledd_vinkler, float* transform);
    void inverse(float* transform, float* jac, float* pinv, float* A_t, 
                 float* AA_t, float* A_tA, float* initial_joint_angles, 
                 float ew, float ev, float max_iterations, float* ledd_vinkler);
    void jacobian(float* ledd_vinkler, float* jacobian);
};

#endif // KINEMATICS1_H
