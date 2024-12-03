#ifndef MATRIXUTILS1_H
#define MATRIXUTILS1_H

#include <Arduino.h>

class MatrixUtils {
public:
    MatrixUtils();

    // Generelle matrise-metoder
    void print_matrix(float* mat, int rows, int cols, String message);
    void copy_matrix(float* source, int rows, int cols, float* destination);
    void identity(float* mat, int size);
    void zero(float* mat, int rows, int cols);
    void transpose(float* mat, int rows, int cols, float* result);
    float trace(float* mat, int size);
    int inverse(float* mat, int size);

    // Metoder for matrisemultiplikasjon
    void mul_matrix(float* mat1, float* mat2, int rows1, int cols1, int rows2, int cols2, float* result);

    // Legg til flere metoder her dersom nødvendig for kinematikk-koden din
};

#endif // MATRIXUTILS1_H
