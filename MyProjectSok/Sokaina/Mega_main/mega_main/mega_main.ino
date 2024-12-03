#include "MatrixUtils1.h"
#include "Kinematics1.h"

#define NUM_JOINTS 3

void setup() {
    Serial.begin(9600);

    // Opprett instanser av Kinematics og MatrixUtils-klasser
    Kinematics kin(NUM_JOINTS);
    MatrixUtils mat_utils;

    // Legg til leddaksene for kinematikmodellen
    kin.add_joint_axis(0, 0, 1);
    kin.add_joint_axis(0, 0, 0);
    kin.add_joint_axis(0, 0, -1);

    // Definer den opprinnelige end-effektorposen for kinematikmodellen
    kin.add_initial_end_effector_pose(-1, 0, 0, 0, 1, 0, 0, 0, 1);

    // Definer leddvinklene for foroverkinematikkberegningen
    float joint_angles[NUM_JOINTS] = {PI / 2.0, 3.0, PI};
    float transform[3][3];

    // Utfør foroverkinematikk for å beregne end-effektortransformasjonen
    kin.forward(joint_angles, (float*)transform);

    // Skriv ut transformasjonsmatrisen
    mat_utils.print_matrix((float*)transform, 3, 3, "Transform");
}

void loop() {
    // Ingen gjentakende kode nødvendig for foroverkinematikk
}
