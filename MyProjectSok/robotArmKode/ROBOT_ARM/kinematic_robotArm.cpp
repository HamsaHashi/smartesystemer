
#include "kinematics.h"
#include "matrixUtils.cpp"

Kinematics::Kinematics(int antall_Ledd){
  antall_ledd = antall_Ledd; 
  antall_ledd_deklarert = 0; 
  ///
  mat_utils.zero((float*)initial_end_effector_pose, 3, 3);
  mat_utils.zero((float*)joint_screw_axes, 3, 3); //float se2[3][3]; ->screw axis (rotation and translation)

}

void Kinematics::leggTil_antall_ledd(float s1, float s2, float s3){
  joint_se2[antall_ledd_deklarert][0] = s1;
  joint_se2[antall_ledd_deklarert][1] = s2;
  joint_se2[antall_ledd_deklarert][2] = s3;

  antall_ledd_deklarert++; 
}

///

void Kinematics::add_initial_end_effector_pose(float m11, float m12, float m13, float m14, float m21, float m22, float m23, float m24, float m31){
  //i en2D transformation matriseskal vi ha =>9 values: 
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



///
void Kinemtaics::forward(float* ledd_vinkler, float* transform){
  float vec3[3]; 
  float sec2[3][3]; 
  float exp3[3][3]; 
  float result[3][3]; 

   
  for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
          transform[3 * i + j] = initial_end_effector_pose[i][j];
      }
  }

    
  for (int i = num_of_joints - 1; i >= 0; i--) {
      mat_utils.mul_scalar(joint_screw_axes[i], joint_angles[i], 1, 3, vec3);
      mat_utils.vec_to_se2(vec3, (float*)se2);
      mat_utils.exp3((float*)se2, (float*)exp3);
      mat_utils.mul_matrix((float*)exp3, (float*)transform, 3, 3, 3, 3, (float*)result);
      mat_utils.copy_matrix((float*)result, 3, 3, (float*)transform);
  }

}
void Kinematics::inverse(float* transform, float* jac, float* pinv, float* A_t, float* AA_t, float* A_tA, float* initial_joint_angles, float ew, float ev, float max_iterations, float* joint_angles) {
  float Tsb[3][3];
  float Tsb_inv[3][3];
  float Tsb_inv_T[3][3];s
  float log3[3][3]];
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
  mat_utils.adjoint((float*)Tsb, (float*)adj);
  mat_utils.mul_vector((float*)adj, vec3, 3, 3, Vs);

  w[0] = Vs[0];
  w[1] = Vs[1];
///////////////////
  v[0] = Vs[3];
  v[1] = Vs[4];
  error = (mat_utils.norm(w) > ew || (mat_utils.norm(v) > ev); 
  i = 0; 

  while (error && i < max_iterations) {
    Serial.print("loop\t");
    Serial.println(i);
    jacobian(joint_angles, (float*)jac);
    mat_utils.pseudo_inverse((float*)jac, (float*)A_t, (float*)AA_t, (float*)A_tA, 3, antall_ledd, (float*)pinv);
    mat_utils.mul_vector((float*)pinv, Vs, antall_ledd, 3, pinv_Vs);
    mat_utils.add_matrix(ledd_vinkler, pinv_Vs, 1, antall_ledd, ledd_vinkler);

    i = i + 1;

        ///
    forward(joint_angles, (float*)Tsb);

    mat_utils.trn_mat_inverse((float*)Tsb, (float*)Tsb_inv);
    mat_utils.mul_matrix((float*)Tsb_inv, (float*)transform, 3, 3, 3, 3, (float*)Tsb_inv_T);
    mat_utils.log3((float*)Tsb_inv_T, (float*)log3);
    mat_utils.se2_to_vec((float*)log3, vec3);
    mat_utils.adjoint((float*)Tsb, (float*)adj);
    mat_utils.mul_vector((float*)adj, vec3, 3, 3, Vs);

    w[0] = Vs[0];
    w[1] = Vs[1];

    v[0] = Vs[3]; 

    error = (mat_utils.norm(w) > ew) || (mat_utils.norm(v) > ev); 
  } 
}


/////JCOBIAN_MATRICES___
void Kinematics::jacobian(float* ledd_vinkler, float* jacobian) {
  float transform[3][3]; 
  float vec3[3]; //linear & angular velocities (3-element vector)1.linear(x direction) 2. linear (y) 3. angular (zNOT INCLUDED) 
  float se2[3][3]; //screw axis (rotation and translation)
  float exp3[3][3]; //exponential map->combines. 
  float result[3][3];//result 
  float adj[3][3]; //
  float jacobian_column[3]; //six types of velocities (3 linear and 3 angular velocities)

  ////
  mat_utils.zero((float*)jacobian, 3, antall_ledd); //since we r workiing on a "2D"
  mat_utils.zero((float*)transform, 4); 

  for (int i = 0; i < 6; i++){
    for(int j = 0; j< antall_ledd; j++){
      jacobian[antall_ledd * i + j] = joint_se2[j][i]; //PS. se ->screw axes

    }
  }
  for(int i = 1; i < antall_ledd; i++){
     mat_utils.mul_scalar(joint_se2[i-1], ledd_vinkler[i-1], 1, 3, vec3);
     mat_utils.vec_to_se2(vec3, (float*)se2);
      mat_utils.exp3((float*)se2, (float*)exp3);

      mat_utils.mul_matrix((float*)transform, (float*)exp3, 3, 3, 3, 3, (float*)result);
      mat_utils.copy_matrix((float*)result, 4, 4, (float*)transform);
      mat_utils.adjoint((float*)transform, (float*)adj);
      mat_utils.mul_vector((float*)adj, joint_se2[i], 3, 3, jacobian_column);
      
        for (int j = 0; j < 6; j++) {
            jacobian[num_of_joints * j + i] = jacobian_column[j];
        }
  }
}

