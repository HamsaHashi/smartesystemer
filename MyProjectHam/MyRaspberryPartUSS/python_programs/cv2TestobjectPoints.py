import cv2
import numpy as np

# Enkle testdata
image_point = np.array([[[0, 0, 0]]], dtype=np.float32)  # Verdenspunkt i origo
rvec = np.array([[0.0], [0.0], [0.0]], dtype=np.float32)  # Ingen rotasjon
tvec = np.array([[0.0], [0.0], [5.0]], dtype=np.float32)  # Kamera 5 enheter foran punktet
mtx = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]], dtype=np.float32)  # Enkel kameramatrise
dist = np.zeros(5, dtype=np.float32)  # Ingen forvrengning

try:
    world_point, _ = cv2.projectPoints(image_point, rvec, tvec, mtx, dist)
    print(f"World point: {world_point}")
except Exception as e:
    print(f"Error in cv2.projectPoints: {e}")
