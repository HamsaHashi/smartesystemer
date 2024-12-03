#ifndef MATRIXUTILS_H
#define MATRIXUTILS_H

#include <Arduino.h>
//#include "Kinematicss.h"

//deklarer fcts + forklaring på hver funksjon

// Klasse for matriseoperasjoner spesifikke for 2D-kinematikk og transformasjoner
class MatrixUtils {
public:
  // Konstruktør
  MatrixUtils();

  // Generelle metoder for matriser
  void print_matrix(float* mat, int r, int c, String message); // Skriver ut matrisen +  melding
  void copy_matrix(float* mat, int r, int c, float* result);   // Kopierer en matrise
  void identity(float* mat, int n);                           // Oppretter en identitetsmatrise
  void zero(float* mat, int r, int c);                        // Fyller en matrise med nuller
  void transpose(float* mat, int r, int c, float* result);    // Transponerer en matrise
  float trace(float* mat, int r);                             // Beregner sporet av en matrise (summen av diagonale elementer)
  int inverse(float* A, int n);                               // Inverterer en matrise (for kvadratiske matriser)

  // Spesifikke metoder for kinematikk
  void pseudoInverse(float* mat, float* transpose, float* product1, float* product2, int rows, int cols, float* result);

  // Transformasjonsmatriser
  void extractRotationMatrix(float* mat, float* rotMat);              // Henter rotasjonsdelen fra en transformasjonsmatrise
  void extractPositionVector(float* mat, float* posVec);              // Henter posisjonsvektoren fra en transformasjonsmatrise
  void createTransformationMatrix(float* rotMat, float* posVec, float* trnMat); // Oppretter en transformasjonsmatrise
  void inverseTransformationMatrix(float* mat, float* result);        // Inverterer en transformasjonsmatrise
  void adjointMatrix(float* mat, float* result);                      // Beregner adjunktmatrisen

  // Eksponentielle og logaritmiske kart for rotasjoner
  void exponentialMap3(float* mat, float* result);  // Beregner eksponentialkart for 3x3 rotasjonsmatriser
  void logarithmMap3(float* mat, float* result);    // Beregner logaritmekart for 3x3 rotasjonsmatriser

  // Vektor- og matriseoperasjoner
  void vectorToSkewSymmetric(float* vec, float* result);              // Konverterer en vektor til en skjev-symmetrisk matrise
  void skewSymmetricToVector(float* mat, float* result);              // Konverterer en skjev-symmetrisk matrise til en vektor
  void transformationToVector(float* trnMat, float* result);          // Konverterer en transformasjonsmatrise til en vektor
  void vectorToTransformation(float* vec, float* result);             // Konverterer en vektor til en transformasjonsmatrise
  void mul_vector(float* mat, float* vec, int r, int c, float* result); // Multipliserer en matrise med en vektor

  // Verktøy for matriser og vektorer
  float calculateNorm(float* vec);                                    // Beregner normen til en vektor
  void addScalarToMatrix(float* mat, float scalar, int rows, int cols, float* result);
  void subtractScalarFromMatrix(float* mat, float scalar, int rows, int cols, float* result);
  void multiplyMatrixByScalar(float* mat, float scalar, int rows, int cols, float* result);
  void divideMatrixByScalar(float* mat, float scalar, int rows, int cols, float* result);
  void addMatrices(float* mat1, float* mat2, int rows, int cols, float* result);
  void subtractMatrices(float* mat1, float* mat2, int rows, int cols, float* result);
  void multiplyMatrices(float* mat1, float* mat2, int rows1, int cols1, int rows2, int cols2, float* result);
  void multiplyMatrixByVector(float* mat, float* vec, int rows, int cols, float* result);

  ///funksjoner jeg glwemte å deklarere :) som brukes i matrixUtils.cpp: 
  void mul_matrix(float* mat1, float* mat2, int r1, int c1, int r2, int c2, float* result);
  void mul_scalar(float* mat, float scalar, int rows, int cols, float* result);
  void trn_mat_inverse(float* mat, float* result);
  void log3(float* mat, float* result);
  void se2_to_vec(float* mat, float* vec);

  ///////
  void vec_to_se2(float* vec, float* result);
  void exp3(float* se2, float* result);


  //funksj som brukes i kin_robotArm.cpp: 
  void leggTil_antall_ledd(float s1, float s2, float s3);

};  

#endif 
