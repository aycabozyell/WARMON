import requests
import mysql.connector
import time
import datetime
import json
import sys

 
connection = mysql.connector.connect(user='root', password='asd', host='127.0.0.1', database='DEUSystemRoomsPiDB')

if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)

cursor = connection.cursor()

cursor.execute("SELECT * FROM Alerts")
data = cursor.fetchone()
#print(data[0])

obj = {"RoomName" : "Room 1", "RoomID" : 1, "AlertName": data[1], "AlertCode" : data[2]}
#print(json.dumps(obj))
data = json.dumps(obj)


api_url = "http://0.0.0.0/"
resp = requests.post(api_url, data)

def saveAlert():
       
 
connection.close()
