# SaaAsema

<H3>Chart.php<H3/>
	
```
  <html>
  <head>
	<?php
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
import time
from datetime import datetime
import mariadb
import Adafruit_DHT

##salasana = "testi123"
##password = 0
##while password == 0:
##    salasana2 = input("Anna salasana: ")
##    if salasana2 == salasana:
##        print("Password correct")
##        password == 1
##        break
##    
##    elif salasana2 != salasana:
##        print("Password incorrect")
##        password == 0
        
##while password == 1:

conn = mariadb.connect(user="root", password="HyTe", host="localhost", database="Tiedot")
cur = conn.cursor()

arvo = 2
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    time.sleep(5)
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if temperature is not None:
        print("Temp={0:0.1f}C".format(temperature))
        aika = (f"{datetime.now()}".split('.')[0])
        print(aika)
        print(f"{temperature}")
        cur.execute(f"INSERT INTO Mittari (arvo, pvm) VALUES ('{temperature}', '{aika}')")
        arvo += 2
    else:
        print("NOT WÖRKING!?!?!");
    conn.commit()
    
conn.close()
```
