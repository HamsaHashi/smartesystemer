import numpy as np
import cv2 as cv
import glob

# Chessboard size (antallet indre krysningspunkter)
chessboardSize = (9, 6)  # Passer til 24x17 sjakkbrett (uten kantstrek)

# Størrelsen på hvert bilde i kalibreringen - bør matche oppløsningen på dine bilder
frameSize = (1440, 1080)  # Bruk samme oppløsning som du har brukt for å ta bildene

# Termination criteria for corner refinement
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Forbered objektskoordinater (3D-punkter) for sjakkbrettet (uten kantstrek)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)

# Arrays for å lagre objektpunkter og bildepunkt
objPoints = []  # 3D-punkter i virkelige verden
imgPoints = []  # 2D-punkter i bildeplanet

# Hent bildene som skal brukes til kalibrering
images = glob.glob('/home/hamsahashi/Desktop/yolo object detection/Calibration_Raspi_Cam/NestSisteBilde_Sjakkbrett/*.jpg')  # Oppdater stien om nødvendig

# Prosesser hvert bilde for å finne hjørner
for image in images:
    print(f"Behandler bilde: {image}")
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Finn sjakkbrett-hjørnene
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE)

    # Hvis hjørnene er funnet, legg til objekt- og bildepunkt
    if ret:
        print(f"Hjørner FUNNET :) i {image}")
        objPoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgPoints.append(corners2)

        # Tegn hjørnene på bildet for kontroll
        cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
    else:
        print(f"Hjørner IKKE funnet i {image}")

cv.destroyAllWindows()

# Utfør kamerakalibrering
if len(objPoints) > 0 and len(imgPoints) > 0:
    ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objPoints, imgPoints, frameSize, None, None)
    print("Kamera kalibrert(ret):", ret)
    print("\nKameramatrise(cameraMatrix):\n", cameraMatrix)
    print("\nForvrengningsparametere(dist):\n", dist)
    print("\nRotasjonsvektorer(rvecs):\n", rvecs)
    print("\nTranslasjonsvektorer(tvecs):\n", tvecs)
else:
    print("Ingen gyldige punkter funnet for kalibrering. Kontroller bildene og sjakkbrettmønsteret.")

# Lagre kalibreringsresultatene i en fil (valgfritt, men nyttig for senere bruk)
np.savez('/home/hamsahashi/Desktop/yolo object detection/Calibration_Raspi_Cam/calibration112_data.npz',
         cameraMatrix=cameraMatrix, dist=dist, rvecs=rvecs, tvecs=tvecs)
print("Kalibreringsdata lagret som 'calibration_data.npz'")

# Forvrenningskorrigering og lagring av testbilde (valgfritt)
img = cv.imread(images[0])  # Bruk ett av kalibreringsbildene for testing
h, w = img.shape[:2]
newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w, h), 1, (w, h))

# Fjern forvrengning
dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)

# Beskjær bildet til ROI (valgfritt)
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('/home/hamsahashi/Desktop/yolo object detection/Calibration_Raspi_Cam/caliResult.png', dst)

# Beregn reprojeksjonsfeil (valgfritt, men nyttig for å evaluere kalibreringens nøyaktighet)
mean_error = 0
for i in range(len(objPoints)):
    imgPoints2, _ = cv.projectPoints(objPoints[i], rvecs[i], tvecs[i], cameraMatrix, dist)
    error = cv.norm(imgPoints[i], imgPoints2, cv.NORM_L2) / len(imgPoints2)
    mean_error += error

print("\nTotal reprojeksjonsfeil: {}".format(mean_error / len(objPoints)))
