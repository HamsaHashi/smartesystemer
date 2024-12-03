#include "matrixUtilss.h"
#include "Kinematicss.h"



Kinematics::Kinematics(int antall_Ledd) { //: mat_utils()
  antall_ledd = antall_Ledd; 
  antall_ledd_deklarert = 0; 
  mat_utils = new MatrixUtils();

  mat_utils.zero((float*)initial_end_effector_pose, 3, 3);
  mat_utils.zero((float*)joint_screw_axes, 3, 3); // Screw axis (rotation and translation)
}
Kinematics::~Kinematics() {
  delete mat_utils;  // Frigjør allokert minne
}


void Kinematics::leggTil_antall_ledd(float s1, float s2, float s3) {
  joint_screw_axes[antall_ledd_deklarert][0] = s1;
  joint_screw_axes[antall_ledd_deklarert][1] = s2;
  joint_screw_axes[antall_ledd_deklarert][2] = s3;

  antall_ledd_deklarert++; 
}

void Kinematics::add_initial_end_effector_pose(float m11, float m12, float m13, float m21, float m22, float m23, float m31, float m32, float m33) {
  initial_end_effector_pose[0][0] = m11;
  initial_end_effector_pose[0][1] = m12;
  initial_end_effector_pose[0][2] = m13;

  initial_end_effector_pose[1][0] = m21;
  initial_end_effector_pose[1][1] = m22;
  initial_end_effector_pose[1][2] = m23;

  initial_end_effector_pose[2][0] = m31;
  initial_end_effector_pose[2][1] = m32;
  initial_end_effector_pose[2][2] = m33;
}

void Kinematics::jacobian(float* ledd_vinkler, float* jacobian_matrix) {
  // Step 1: Initialize variables
  float transform[3][3];
  float vec3[3];
  float se2[3][3];
  float exp3[3][3];
  float result[3][3];
  float adj[3][3];
  float jacobian_column[3];

  // Zero the Jacobian matrix
  mat_utils.zero(jacobian_matrix, 2, antall_ledd); // 2 rows for planar (x, y)

  // Forward kinematics transformations for all joints
  mat_utils.identity((float*)transform, 3); // Start with identity for the base

  for (int i = 0; i < antall_ledd; i++) {
    // Calculate the screw axis and exponential map
    mat_utils.mul_scalar(joint_screw_axes[i], ledd_vinkler[i], 1, 3, vec3);
    mat_utils.vec_to_se2(vec3, (float*)se2);
    mat_utils.exp3((float*)se2, (float*)exp3);

    // Update the transformation
    mat_utils.mul_matrix((float*)transform, (float*)exp3, 3, 3, 3, 3, (float*)result);
    mat_utils.copy_matrix((float*)result, 3, 3, (float*)transform);

    // Compute the adjoint representation
    mat_utils.adjointMatrix((float*)transform, (float*)adj);

    // Multiply adjoint by the screw axis for the current joint
    mat_utils.mul_vector((float*)adj, joint_screw_axes[i], 3, 3, jacobian_column);

    // Add the Jacobian column to the matrix
    jacobian_matrix[i] = jacobian_column[0]; // x-direction velocity
    jacobian_matrix[antall_ledd + i] = jacobian_column[1]; // y-direction velocity
  }
}



void Kinematics::forward(float* ledd_vinkler, float* transform) {
  float vec3[3]; 
  float se2[3][3]; 
  float exp3[3][3]; 
  float result[3][3]; 

  // Initialize the transform matrix with the initial end effector pose (3x3 for 2D)
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      transform[3 * i + j] = initial_end_effector_pose[i][j];
    }
  }

  // Iterate through each joint angle in reverse to apply the transformations
  for (int i = antall_ledd - 1; i >= 0; i--) {
    mat_utils.mul_scalar(joint_screw_axes[i], ledd_vinkler[i], 1, 3, vec3);
    mat_utils.vec_to_se2(vec3, (float*)se2);
    mat_utils.exp3((float*)se2, (float*)exp3);
    mat_utils.mul_matrix((float*)exp3, (float*)transform, 3, 3, 3, 3, (float*)result);
    mat_utils.copy_matrix((float*)result, 3, 3, (float*)transform);
  }
}

bool Kinematics::inverse(float* transform, float* jac, float* pinv, float* A_t, float* AA_t, float* A_tA, float* initial_joint_angles, float ew, float ev, float max_iterations, float* ledd_vinkler) {
  //for  avbryte funksjonen umiddelbart dersom parameteren er ugyldige
  if (max_iterations <= 0) {
    Serial.println("Error: max_iterations must be greater than 0.");
    return false;
  }
  
  float Tsb[3][3];
  float Tsb_inv[3][3];
  float Tsb_inv_T[3][3];
  float log3[3][3];
  float vec3[3];
  float adj[3][3];
  float Vs[3];
  float w[2];
  float v[2];
  float pinv_Vs[3];
  bool error;
  int i;

  mat_utils.copy_matrix(initial_joint_angles, 1, antall_ledd, ledd_vinkler);
  forward(ledd_vinkler, (float*)Tsb);
  mat_utils.trn_mat_inverse((float*)Tsb, (float*)Tsb_inv);
  mat_utils.mul_matrix((float*)Tsb_inv, (float*)transform, 3, 3, 3, 3, (float*)Tsb_inv_T);
  mat_utils.log3((float*)Tsb_inv_T, (float*)log3);
  mat_utils.se2_to_vec((float*)log3, vec3);
  mat_utils.adjointMatrix((float*)Tsb, (float*)adj);
  mat_utils.mul_vector((float*)adj, vec3, 3, 3, Vs);

  w[0] = Vs[0];
  w[1] = Vs[1];
  v[0] = Vs[2];
  v[1] = Vs[3];

  error = (mat_utils.calculateNorm(w) > ew || mat_utils.calculateNorm(v) > ev);
  i = 0;

  while (error && i < max_iterations) {
    Serial.print("Loop iteration: ");
    Serial.println(i);

    jacobian(ledd_vinkler, (float*)jac);

    // Call pseudo-inverse and check its result
    if (!mat_utils.pseudoInverse((float*)jac, (float*)A_t, (float*)AA_t, (float*)A_tA, 3, antall_ledd, (float*)pinv)) {
      Serial.println("Error: Pseudo-inverse calculation failed.");
      return false;
    }
    ////////mat_utils.pseudoInverse((float*)jac, (float*)A_t, (float*)AA_t, (float*)A_tA, 3, antall_ledd, (float*)pinv);
    
    
    mat_utils.mul_vector((float*)pinv, Vs, antall_ledd, 3, pinv_Vs);
    mat_utils.addMatrices(ledd_vinkler, pinv_Vs, 1, antall_ledd, ledd_vinkler);

    i++;

    forward(ledd_vinkler, (float*)Tsb);
    mat_utils.trn_mat_inverse((float*)Tsb, (float*)Tsb_inv);
    mat_utils.mul_matrix((float*)Tsb_inv, (float*)transform, 3, 3, 3, 3, (float*)Tsb_inv_T);
    mat_utils.log3((float*)Tsb_inv_T, (float*)log3);
    mat_utils.se2_to_vec((float*)log3, vec3);
    mat_utils.adjointMatrix((float*)Tsb, (float*)adj);
    mat_utils.mul_vector((float*)adj, vec3, 3, 3, Vs);

    w[0] = Vs[0];
    w[1] = Vs[1];
    v[0] = Vs[2];
    v[1] = Vs[3];

    error = (mat_utils.calculateNorm(w) > ew || mat_utils.calculateNorm(v) > ev);
  }
  return !error;
}

