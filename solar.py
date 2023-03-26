import json
from gpiozero import LED
from time import sleep
import requests

varLed = LED(18)
url = "https://data.buienradar.nl/2.0/feed/json"

# als varW 1 is, dan is er een wens om te wassen
varW = 1

while True:
  res = requests.get(url)
  data = res.json()

  stations = data["actual"]["stationmeasurements"]
  sunpower = 0
  for s in stations:
    if s["stationname"] == "Meetstation De Bilt":
      sunpower = int(s["sunpower"])
      break

  print("De sunpower is nu", sunpower)

  if sunpower > 300:
    if varW == 1:
      # zet de led aan
      varLed.on()

      # zet de wasmachine handmatig aan
      # indien mogelijk, schakel de wasmachine op afstand
      print("Er kan gewassen worden")

      varW = 0

  else:
    print("Wacht 15 minuten")
    sleep(60 * 15)
