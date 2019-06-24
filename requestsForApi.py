import requests
import json
import time
import datetime
import sys
import mysql.connector

connection = mysql.connector.connect(user='root', password='asd', host='127.0.0.1', database='WARMON')
AlarmAPIurl= "http://192.168.1.101:86/api/Alarm"

datax = {
	"Room_Code":"25",
	"Alert_Code":"02",
	"IsAlertOn":"true",
	"Read_Date":"2019-06-11T12:24:00.044Z"
	
}
headerxs = {'content-type': 'application/json',
            'SecretKey' : 'H6Yv2nZZ3Hby3kwCNmPt4Rbxe8p5pA96'
            }


cursor = connection.cursor(buffered= True)

r = requests.post(url=AlarmAPIurl,data=json.dumps(datax), headers= headerxs)
pastebin_url= r.text
print("The pastebin URL: %s \n"%pastebin_url)

"""
if ( r.status_code == 200 ):
    print("data saved in db")
    sqlquery = ""INSERT INTO Alerts (Alert_Id, Alert_Name, Alert_Code) VALUES (%s , %s, %s)""
    degisken = obj.Alert_Name
    degisken2 = obj.Alert_Code
    value = ("NULL",degisken, degisken2)
    cursor.execute(sqlquery, value)
    connection.commit()
    
    print(cursor.rowcount,"kaydedildi !")
"""  
    


EnvironmentAPIurl= "http://192.168.1.101:86/api/Environment"

dataa = {
	"Room_Code":"25",
	"Temperature":30,
	"Humidity":"20",
	"Read_Date":"2019-06-11T12:24:00.044Z"
	
}


headersa = {'content-type': 'application/json'}
r= requests.post(url=EnvironmentAPIurl,data=json.dumps(dataa),headers= headersa)
pastebin_url= r.text
print("The pastebin URL: %s"%pastebin_url)

print(datetime.datetime.now())


    
