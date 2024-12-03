#include "MatrixUtils1.h"

// Constructor
MatrixUtils::MatrixUtils() {}

// Generelle matrise-metoder
void MatrixUtils::print_matrix(float* mat, int rows, int cols, String message) {
    Serial.println(message);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            Serial.print(mat[cols * i + j]);
            Serial.print("\t");
        }
        Serial.println();
    }
    Serial.println();
}

void MatrixUtils::copy_matrix(float* source, int rows, int cols, float* destination) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            destination[cols * i + j] = source[cols * i + j];
        }
    }
}

void MatrixUtils::identity(float* mat, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            mat[size * i + j] = (i == j) ? 1 : 0;
        }
    }
}

void MatrixUtils::zero(float* mat, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            mat[cols * i + j] = 0;
        }
    }
}

void MatrixUtils::transpose(float* mat, int rows, int cols, float* result) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[rows * j + i] = mat[cols * i + j];
        }
    }
}

float MatrixUtils::trace(float* mat, int size) {
    float sum = 0;
    for (int i = 0; i < size; i++) {
        sum += mat[size * i + i];
    }
    return sum;
}

// Matrisesnufunksjon ved hjelp av Gauss-eliminasjon
int MatrixUtils::inverse(float* mat, int size) {
    int pivrow = 0;
    int pivrows[6];
    float tmp;

    for (int k = 0; k < size; k++) {
        tmp = 0;
        for (int i = k; i < size; i++) {
            if (abs(mat[i * size + k]) >= tmp) {
                tmp = abs(mat[i * size + k]);
                pivrow = i;
            }
        }

        if (mat[pivrow * size + k] == 0.0f) return 0;

        if (pivrow != k) {
            for (int j = 0; j < size; j++) {
                tmp = mat[k * size + j];
                mat[k * size + j] = mat[pivrow * size + j];
                mat[pivrow * size + j] = tmp;
            }
        }
        pivrows[k] = pivrow;

        tmp = 1.0f / mat[k * size + k];
        mat[k * size + k] = 1.0f;
        for (int j = 0; j < size; j++) {
            mat[k * size + j] *= tmp;
        }

        for (int i = 0; i < size; i++) {
            if (i != k) {
                tmp = mat[i * size + k];
                mat[i * size + k] = 0.0f;
                for (int j = 0; j < size; j++) {
                    mat[i * size + j] -= mat[k * size + j] * tmp;
                }
            }
        }
    }

    for (int k = size - 1; k >= 0; k--) {
        if (pivrows[k] != k) {
            for (int i = 0; i < size; i++) {
                tmp = mat[i * size + k];
                mat[i * size + k] = mat[i * size + pivrows[k]];
                mat[i * size + pivrows[k]] = tmp;
            }
        }
    }
    return 1;
}

void MatrixUtils::mul_matrix(float* mat1, float* mat2, int rows1, int cols1, int rows2, int cols2, float* result) {
    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols2; j++) {
            result[cols2 * i + j] = 0;
            for (int k = 0; k < cols1; k++) {
                result[cols2 * i + j] += mat1[cols1 * i + k] * mat2[cols2 * k + j];
            }
        }
    }
}

// Flere metoder kan legges til her hvis nødvendig for kinematikk-koden din
