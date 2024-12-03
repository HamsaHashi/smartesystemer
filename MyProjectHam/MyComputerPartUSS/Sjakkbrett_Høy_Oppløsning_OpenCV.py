import cv2 as cv
import numpy as np

# Størrelse på sjakkbrettet
cols = 24  # Antall kolonner (anbefalt: 24 for flere krysningspunkter)
rows = 17  # Antall rader (anbefalt: 17 for flere krysningspunkter)
square_size = 150  # Størrelse på hver rute i piksler (anbefalt: 150 eller 200 for høyoppløsning)

# Beregn størrelse på bildet basert på antall ruter og størrelse på hver rute
width = cols * square_size
height = rows * square_size

# Lag et hvitt bilde med en svart ramme rundt
image = np.ones((height + 2 * square_size, width + 2 * square_size), dtype=np.uint8) * 255

# Tegn sjakkbrettmønsteret
for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            top_left_x = j * square_size + square_size
            top_left_y = i * square_size + square_size
            cv.rectangle(image, (top_left_x, top_left_y), 
                         (top_left_x + square_size, top_left_y + square_size), 0, -1)

# Tegn en ramme rundt hele sjakkbrettet
cv.rectangle(image, (square_size, square_size), 
             (width + square_size, height + square_size), 0, 2)

# Lagre bildet i ønsket katalog
output_path = r"C:\Users\Hamsa\OneDrive\Skrivebord\chessboard_highresxxx_24x17.png"
cv.imwrite(output_path, image)

print(f"Sjakkbrettmønster lagret som {output_path}")
