
import numpy as np
import cv2

def load_calibration_data():
    calibration_path = "/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/USSresources/USSmodel/calibration112_data.npz"
    
    # Laster inn kalibreringsdata fra filen min
    data = np.load(calibration_path)
    mtx = data['cameraMatrix']
    dist = data['dist']
    rvecs = data['rvecs']
    tvecs = data['tvecs']
    frame_width, frame_height = 960, 720
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (frame_width, frame_height), 1, (frame_width, frame_height))
    
     # Sørg for at dist er en 1D-array
    if len(dist.shape) > 1:
        dist = dist.flatten()
    
    return mtx, dist, newcameramtx, roi, rvecs, tvecs


