#Henta datasettet fra roboflow.com, lastet ned apki key så jeg slapp å laste ned zipfil med alle bildene
from roboflow import Roboflow
rf = Roboflow(api_key="dSmfIKkJM599mknVb3kd")
project = rf.workspace("baloon-f12iq").project("baloon-detection-olq38")
version = project.version(6)
dataset = version.download("yolov8-obb")
# verifiseringsmetodene for å sikre at bildene, annotasjonene, og data.yaml-filen er riktig.
# 1. Finn nedlastet datasett. skal være en mappe med navn dataset typeshit.
#   den skal inneholde bilder en mappe som heter train/val typeshit
#   Annotasjoner. tekstfil .txt for hvert bilde i samme mappe som bildene
#   data.yaml-fil den ligger i datasett mappen og inneholder info om stiene til bildene og klassene
# 2. Verifisere bilder(sjekk format skal være en av -> .jpg/.png/.bmp)
#   åpne noen av bildene og sjekk om det ser riktig ut kvalitet og innehold.

