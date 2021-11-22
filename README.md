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
