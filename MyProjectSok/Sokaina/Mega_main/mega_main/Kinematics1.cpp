#include "Kinematics1.h"

Kinematics::Kinematics(int antall_Ledd) {
    antall_ledd = antall_Ledd;
    antall_ledd_deklarert = 0;
    mat_utils.zero((float*)initial_end_effector_pose, 3, 3);
    mat_utils.zero((float*)joint_screw_axes, 3, 3);
}

void Kinematics::add_joint_axis(float s1, float s2, float s3) {
    joint_screw_axes[antall_ledd_deklarert][0] = s1;
    joint_screw_axes[antall_ledd_deklarert][1] = s2;
    joint_screw_axes[antall_ledd_deklarert][2] = s3;
    antall_ledd_deklarert++;
}

void Kinematics::add_initial_end_effector_pose(float m11, float m12, float m13,
                                               float m21, float m22, float m23,
                                               float m31, float m32, float m33) {
    initial
