import numpy as np

data = np.load("/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/USSresources/USSmodel/calibration112_data.npz")
print("Keys:", data.keys())
print("rvecs:", data.get('rvecs'))
print("tvecs:", data.get('tvecs'))
