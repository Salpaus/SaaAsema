import time
from datetime import datetime
import mariadb

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

while True:
    time.sleep(5)
    print(f"{datetime.now()}".split('.')[0])
    cur.execute(f"INSERT INTO Mittari (arvo, pvm) VALUES ('{arvo}', '{datetime.now()}')")
    arvo += 2
    conn.commit()
    
conn.close()

