#include "matrixUtils.h"


MatrixUtils::MatrixUtils() {}

/
void MatrixUtils::print_matrix(float* mat, int r, int c, String message) {
    Serial.println(message);
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            Serial.print(mat[c * i + j]);
            Serial.print("\t");
        }
        Serial.println();
    }
    Serial.println();
}

void MatrixUtils::copy_matrix(float* mat, int r, int c, float* result) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            result[c * i + j] = mat[c * i + j];
        }
    }
}

void MatrixUtils::identity(float* mat, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            mat[n * i + j] = (i == j) ? 1 : 0;
        }
    }
}

void MatrixUtils::zero(float* mat, int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            mat[c * i + j] = 0;
        }
    }
}

void MatrixUtils::transpose(float* mat, int r, int c, float* result) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            result[r * j + i] = mat[c * i + j];
        }
    }
}

float MatrixUtils::trace(float* mat, int r) {
    float sum = 0;
    for (int i = 0; i < r; i++) {
        sum += mat[r * i + i];
    }
    return sum;
}


int MatrixUtils::inverse(float* A, int n) {
    int pivrow = 0;
    int pivrows[6];
    float tmp;

    for (int k = 0; k < n; k++) {
        tmp = 0;
        for (int i = k; i < n; i++) {
            if (abs(A[i * n + k]) >= tmp) {
                tmp = abs(A[i * n + k]);
                pivrow = i;
            }
        }

        if (A[pivrow * n + k] == 0.0f) return 0;

        if (pivrow != k) {
            for (int j = 0; j < n; j++) {
                tmp = A[k * n + j];
                A[k * n + j] = A[pivrow * n + j];
                A[pivrow * n + j] = tmp;
            }
        }
        pivrows[k] = pivrow;

        tmp = 1.0f / A[k * n + k];
        A[k * n + k] = 1.0f;
        for (int j = 0; j < n; j++) {
            A[k * n + j] *= tmp;
        }

        for (int i = 0; i < n; i++) {
            if (i != k) {
                tmp = A[i * n + k];
                A[i * n + k] = 0.0f;
                for (int j = 0; j < n; j++) {
                    A[i * n + j] -= A[k * n + j] * tmp;
                }
            }
        }
    }

    for (int k = n - 1; k >= 0; k--) {
        if (pivrows[k] != k) {
            for (int i = 0; i < n; i++) {
                tmp = A[i * n + k];
                A[i * n + k] = A[i * n + pivrows[k]];
                A[i * n + pivrows[k]] = tmp;
            }
        }
    }
    return 1;
}



void MatrixUtils::mul_matrix(float* mat1, float* mat2, int r1, int c1, int r2, int c2, float* result) {
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            result[c2 * i + j] = 0;
            for (int k = 0; k < c1; k++) {
                result[c2 * i + j] += mat1[c1 * i + k] * mat2[c2 * k + j];
            }
        }
    }
}

