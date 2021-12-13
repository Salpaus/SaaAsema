# SaaAsema

<H3>Chart.php<H3/>
	
```
  <html>
  <head>
	<?php
	//Tästä alkaa php koodi. Koodi yhdistää MariaDB tietokantaan ja ottaa tiedon, mikä tallennettiin python koodilla.
	header("refresh: 3;");
	$hostname = "localhost";
	$username = "root";
	$password = "HyTe";
	$db = "Tiedot";
	$dbconnect=mysqli_connect($hostname,$username,$password,$db);
	if ($dbconnect->connect_error) {
		die("Database connection failed: " . $dbconnect->connect_error);
	}
	$query = mysqli_query($dbconnect, "SELECT * FROM Mittari ORDER BY Id DESC")
	or die (mysqli_error($dbconnect));
	?>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
	    
    // Tästä alkaa JavaScript koodi. Koodi piirtää tietokannasta tulleesta datasta taulokon. Taulukko toimii Google charttina. Taulukkoon tulostuu mittauksen kellonaika ja lämpötila.
	    
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

	function drawChart() {
		var data = google.visualization.arrayToDataTable([
			['Aika', 'Arvo'],
			<?php
			while ($row = mysqli_fetch_array($query)) {
				echo "['".$row["pvm"]."', ".$row["arvo"]."],";
			}
			?>
        ]);

        var options = {
          title: 'Sääasema',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="curve_chart" style="width: 900px; height: 500px"></div>
  </body>
</html>
```

<H3>Anturi.py<H3/>
	
```
	
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
```

![asdasdtrghhjkhuikthujk](https://user-images.githubusercontent.com/91182746/145800378-96aabccc-7fe7-424e-b41a-5e0bbd370b8d.PNG)

