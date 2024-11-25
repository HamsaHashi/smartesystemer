#ifndef MATRIXUTILS_H
#define MATRIXUTILS_H

#include <Arduino.h>

class MatrixUtils {
public:
    MatrixUtils();

    
    void printMatrix(float* mat, int rows, int cols, String message);
    void copyMatrix(float* source, int rows, int cols, float* destination);
    void identityMatrix(float* mat, int size);
    void zeroMatrix(float* mat, int rows, int cols);
    void transposeMatrix(float* mat, int rows, int cols, float* result);
    float calculateTrace(float* mat, int size);
    int invertMatrix(float* mat, int size);

    
    void pseudoInverse(float* mat, float* transpose, float* product1, float* product2, int rows, int cols, float* result);

    // Transformation matrix funksjoner
    void extractRotationMatrix(float* mat, float* rotMat);
    void extractPositionVector(float* mat, float* posVec);
    void createTransformationMatrix(float* rotMat, float* posVec, float* trnMat);
    void inverseTransformationMatrix(float* mat, float* result);
    void adjointMatrix(float* mat, float* result);

    // Exponential og logarithmic map methods for rotasjon
    void exponentialMap3(float* mat, float* result);
    void exponentialMap6(float* mat, float* result);
    void logarithmMap3(float* mat, float* result);
    void logarithmMap6(float* mat, float* result);

    // Vector and matrix conversion methods
    void vectorToSkewSymmetric(float* vec, float* result);
    void skewSymmetricToVector(float* mat, float* result);
    void transformationToVector(float* trnMat, float* result);
    void vectorToTransformation(float* vec, float* result);

    // Vector and matrix utility methods
    float calculateNorm(float* vec);
    float getRotationAngle(float* vec);
    void addScalarToMatrix(float* mat, float scalar, int rows, int cols, float* result);
    void subtractScalarFromMatrix(float* mat, float scalar, int rows, int cols, float* result);
    void multiplyMatrixByScalar(float* mat, float scalar, int rows, int cols, float* result);
    void divideMatrixByScalar(float* mat, float scalar, int rows, int cols, float* result);
    void addMatrices(float* mat1, float* mat2, int rows, int cols, float* result);
    void subtractMatrices(float* mat1, float* mat2, int rows, int cols, float* result);
    void multiplyMatrices(float* mat1, float* mat2, int rows1, int cols1, int rows2, int cols2, float* result);
    void multiplyMatrixByVector(float* mat, float* vec, int rows, int cols, float* result);
};

#endif // MATRIXUTILS_H
