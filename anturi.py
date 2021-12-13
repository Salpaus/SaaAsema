##Tämä koodi ottaa anturista dataa ja siirtää sen MariaDB tietokantaan 

import time
from datetime import datetime
import mariadb
import Adafruit_DHT

conn = mariadb.connect(user="root", password="HyTe", host="localhost", database="Tiedot")
cur = conn.cursor()

arvo = 2
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

##Koodissa on 5 sekunnin loop, jonka aikana koodi siirtää anturidatan ja sen hetkisen kellonajan, jos anturi ei saa tietoa se tulostaa "Ei tietoa"

while True:
    time.sleep(5)
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if temperature is not None:
        print("Temp={0:0.1f}C".format(temperature))
        aika = (f"{datetime.now()}".split('.')[0])
        print(aika)
        cur.execute(f"INSERT INTO Mittari (arvo, pvm) VALUES ('{temperature}', '{aika}')")
        arvo += 2
    else:
        print("Ei tietoa")
    conn.commit()

conn.close()

