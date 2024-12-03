#include "matrixUtilss.h"

// Constructor
MatrixUtils::MatrixUtils() {}

// General matrix methods
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

//HJEELPE FUNKSJONER:
void MatrixUtils::log3(float* mat, float* result) {
    // for en 2D transformation matrix, extract rotation and translation components
    float theta = atan2(mat[1], mat[0]); // Extract rotation angle (theta)
    result[0] = 0;
    result[1] = -theta;
    result[2] = mat[2]; // Translation x
    result[3] = theta;
    result[4] = 0;
    result[5] = mat[5]; // Translation y
    result[6] = 0;
    result[7] = 0;
    result[8] = 0;
}


//calculateNorm-The Euclidean norm of a vector.
float MatrixUtils::calculateNorm(float* vec) {
    return sqrt(vec[0] * vec[0] + vec[1] * vec[1] + vec[2] * vec[2]);
}
//add matrices: 2 matrices element wise: 
void MatrixUtils::addMatrices(float* mat1, float* mat2, int rows, int cols, float* result) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[cols * i + j] = mat1[cols * i + j] + mat2[cols * i + j];
        }
    }
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

//adjoint matrix 
void MatrixUtils::adjointMatrix(float* mat, float* result) {
    result[0] = mat[0]; // Rotation component
    result[1] = mat[1];
    result[2] = 0;
    result[3] = mat[3];
    result[4] = mat[4];
    result[5] = 0;
    result[6] = mat[2]; // Translation components
    result[7] = mat[5];
    result[8] = 1;
}

//konverterer en SE(2)-matrise til en vektor (vec3) 
void MatrixUtils::se2_to_vec(float* mat, float* vec) {
    vec[0] = mat[1];  // Angular velocity (rotation)
    vec[1] = mat[2];  // Linear velocity x
    vec[2] = mat[5];  // Linear velocity y
}
// PS.konverterer en vektor (vec3) til en SE(2)-matrise (Special Euclidean group for 2D). En SE(2)-matrise kombinerer rotasjon og translasjon i 2D-rom.

void MatrixUtils::vec_to_se2(float* vec, float* result) {
    // Konverter en 3-element vektor til en SE(2) matrise
    result[0] = 0;
    result[1] = -vec[2];
    result[2] = vec[0];
    result[3] = vec[2];
    result[4] = 0;
    result[5] = vec[1];
    result[6] = 0;
    result[7] = 0;
    result[8] = 0;
}

//PS.beregner den eksponentielle kartleggingen av en SE(2)-matrise. Den tar en SE(2)-matrise som input og genererer en ny matrise som representerer en jevn bevegelse langs den matrisen.

void MatrixUtils::exp3(float* se2, float* result) {
    // Beregn eksponentiell map for en SE(2) matrise
  result[0] = 1 + se2[0];
  result[1] = se2[1];
  result[2] = se2[2];
  result[3] = se2[3];
  result[4] = 1 + se2[4];
  result[5] = se2[5];
  result[6] = se2[6];
  result[7] = se2[7];
  result[8] = 1 + se2[8];
}


// Matrix inversion using Gaussian elimination
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

    if (A[pivrow * n + k] == 0.0f){
      return 0;
    }
      //return 0;

        // Swap rows
    if (pivrow != k) {
      for (int j = 0; j < n; j++) {
        tmp = A[k * n + j];
        A[k * n + j] = A[pivrow * n + j];
        A[pivrow * n + j] = tmp;
      }
    }
    pivrows[k] = pivrow;

        // Normalize pivot row
    tmp = 1.0f / A[k * n + k];
    A[k * n + k] = 1.0f;
    for (int j = 0; j < n; j++) {
      A[k * n + j] *= tmp;
  }

        // Eliminate column
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

    // Restore row order
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

// Matrix multiplication
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

void MatrixUtils::mul_vector(float* mat, float* vec, int r, int c, float* result) {
    for (int i = 0; i < r; i++) {
        result[i] = 0;
        for (int j = 0; j < c; j++) {
            result[i] += mat[c * i + j] * vec[j];
        }
    }
}


void MatrixUtils::mul_scalar(float* mat, float scalar, int rows, int cols, float* result) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[cols * i + j] = mat[cols * i + j] * scalar;
        }
    }
}
void MatrixUtils::trn_mat_inverse(float* mat, float* result) {
    // Implement inverse logic for 2D transformation matrices
    result[0] = mat[0];
    result[1] = mat[3];
    result[3] = mat[1];
    result[4] = mat[4];

    result[2] = -(result[0] * mat[2] + result[1] * mat[5]);
    result[5] = -(result[3] * mat[2] + result[4] * mat[5]);

    result[6] = 0.0f;
    result[7] = 0.0f;
    result[8] = 1.0f;
}

void transpose(float* mat, int r, int c, float* result) {
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      result[r * j + i] = mat[c * i + j];
    }
  }
}

void MatrixUtils::pseudoInverse(float* mat, float* transpose, float* product1, float* product2, int rows, int cols, float* result) {
  // Compute transpose of the matrix
  this->transpose(mat, r, c, result);

  // Multiply transpose with the original matrix
  this->mul_matrix(float* mat1, float* mat2, int r1, int c1, int r2, int c2, float* result);
  //this->mul_matrix(transpose, mat, cols, rows, rows, cols, product1);

  // Compute the inverse of the product
  if (!this->inverse(product1, cols)) {
      Serial.println("Matrix inversion failed!");
      return;
  }

  // Multiply the inverse with the transpose
  this->mul_matrix(float* mat1, float* mat2, int r1, int c1, int r2, int c2, float* result);
}
