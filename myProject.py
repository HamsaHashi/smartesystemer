from ultralytics import YOLO

# YOLO-modellen ferdig trent opp
model = YOLO('yolov8n.pt')

results = model(source = 0, show = True, conf = 0.4, save = False)
""""
OPPGAVER:
laste ned datasettet for å trene modellen på riktig måte
""""""
Trinn 1: Samle data
Før du trener modellen, trenger du en datasett med bilder som inneholder runde baller i forskjellige farger. Du må også annotere (markere) disse ballene i bildene.

a. Samle bilder:
Ta bilder av ballene i forskjellige miljøer og belysning, slik at modellen lærer å kjenne igjen ballene under forskjellige forhold.
Sørg for å inkludere ballene i forskjellige vinkler og avstander.
b. Annotere bildene:
For å annotere bildene kan du bruke et verktøy som LabelImg for å lage bounding boxes rundt ballene i hvert bilde. LabelImg støtter YOLO-formatet, som er nødvendig for treningsprosessen.

Last ned og installer LabelImg:

Følg instruksjonene på LabelImg GitHub.
Sørg for at du lagrer annotasjonene i YOLO-format.
Annoter hver ball i bildene dine:

Opprett to klasser: "gul ball" og "rød ball".
Marker de runde ballene i hvert bilde, og spesifiser riktig klasse.
Lagre annotasjonene i samme katalog som bildene. For hver bildefil (f.eks. image1.jpg), vil det være en tilsvarende annotasjonsfil (f.eks. image1.txt) som inneholder koordinatene for de annoterte objektene.
"""