import time
import datetime
import json
import sys
import random

# initialize GPIO
import mysql.connector


class DemoObj:
    def __init__(self):
        print('hiii')

"""
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
"""

connection = mysql.connector.connect(user='root', password='asd', host='127.0.0.1', database='DEUSystemRoomsPiDB')

if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)

cursor = connection.cursor()


add_employee = ("INSERT INTO Alerts (Alert_Id,Alert_Name,Alert_Code) VALUES ('NULL','ASD Sensor','2')")
cursor.execute(add_employee)
result = cursor.fetchone()

"""
delete_employee = ("DELETE FROM Alerts WHERE Alert_Code = 5")
cursor.execute(delete_employee)
result = cursor.fetchone()
"""

"""
cursor.execute("SELECT * FROM Alerts")
for row in cursor.fetchall():
        print(row[0],row[1],row[2])
"""

"""
for temp in range(1):
    temp = random.randint(20,30)
    print("Temp = %d" % temp)

for humidity in range(1):
    humiditytemp = random.randint(10,40)
    print("Humidity = %d" % humiditytemp)

for smoke in range(1):
    smoke = random.randint(0,1)
    print("Smoke = %d" % smoke)
    
for motion in range(1):
    motion = random.randint(0,1)
    print("motion = %d" % motion)

if temp < 25 && temp >= 27:
"""

while False:
    
    if motionOn == 1:
        print("Hareket Algilandi")
    if motionOn == 0:
        print("Hareket Algilanmadi")
        
    result = instance.read()
    if result.is_valid():
        print("Son okunma tarihi: " + str(datetime.datetime.now()))
        print("Sicaklik: %d C" % temperature)
        print("Nem: %d %%" % humidity)
        
    if smokeOn == 1:
        print("Duman Algilandi")
    if smokeOn == 0:
        print("Duman Algilanmadi")
    time.sleep(1)

    connection.close()

