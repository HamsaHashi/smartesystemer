#ifndef KINEMATICS_H
#define KINEMATICS_H

//#include "matrixUtilss.h"
#include <Arduino.h>
class MatrixUtils;  // Forward declaration



// Klasse for kinematikkberegninger for en robotarm i et 2D-plan
class Kinematics {
private:
  int antall_ledd;               // Totalt antall ledd i robotarmen
  int antall_ledd_deklarert;     // Antall ledd som er definert så langt
  float joint_screw_axes[3][3];  // Matrise for å lagre skruvektorer for alle ledd
  float initial_end_effector_pose[3][3]; // Startposisjon for endeeffektor i 2D
  MatrixUtils mat_utils;         // Objekt for matriseoperasjoner

public:
  // Konstruktør
  Kinematics(int antall_Ledd);
    //destruktør- for å frigjøre minnet når Kinematics-objektet destrueres.
  ~Kinematics();

  // Legg til leddakse
  void add_joint_axis(float s1, float s2, float s3);

  // Legg til initial posisjon for endeeffektor (3x3 matrise i 2D-rom)
  void add_initial_end_effector_pose(float m11, float m12, float m13, 
                                      float m21, float m22, float m23, 
                                      float m31, float m32, float m33);

  // Fremover-kinematikk: Beregn endeeffektorens posisjon basert på leddvinkler
  void forward(float* ledd_vinkler, float* transform);

  // Invers kinematikk: Beregn leddvinkler for å nå en gitt endeeffektorposisjon
  bool inverse(float* transform, float* jac, float* pinv, float* A_t, 
                float* AA_t, float* A_tA, float* initial_joint_angles, 
                float ew, float ev, float max_iterations, float* ledd_vinkler);

  // Beregn Jacobian-matrise for å analysere bevegelse og hastighet
  //void jacobian(float* ledd_vinkler, float* jacobian);
  void jacobian(float* joint_angles, float* jacobian_matrix); // Calculates Jacobian matrix

  /////
  void leggTil_antall_ledd(float s1, float s2, float s3);


};

#endif