import RPi.GPIO as GPIO
import dht11
import time
import datetime
from datetime import timedelta
import json
import sys
import requests
import mysql.connector

#connectionString
connection = mysql.connector.connect(user='root', password='asd', host='127.0.0.1', database='WARMON')
cursor = connection.cursor()
AlarmAPIurl= "http://localhost:80/example"
#"http://192.168.1.101:86/api/Alarm"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pins 18, 17 and 14 
motionPin = 18
tempHumiPin = 14
smokePin = 17
instance = dht11.DHT11(pin=tempHumiPin)
motionOn = 0
smokeOn =0

MaxTemp = 0
MaxHum = 0
MinTemp = 100
MinHum = 100

FromEmreMinTemp = 24
FromEmreMaxTemp = 27
FromEmreMinHum = 20
FromEmreMaxHum = 35

roomCode = 25

list1 = []
list2 = []

sensor_Id1 = 1 
sensor_Id2 = 2

sensor_Type = "AI"

 #postAlert[5] = 

"""
tempHumUnreadCounter = 0

#room infomation
recordRoomId = 1
recordRoomName = "ARGEMERA"


selectQuery= "Select Alert_Code from Alerts where Alert_Name = 'Alarm Yok'"
cursor.execute(selectQuery)
recordAlert = cursor.fetchone()            
connection.commit()



selectQuery= "Select Device_Id from Devices where Device_Name = 'Nem Sicaklik Sensoru'"
cursor.execute(selectQuery)
recordDevice = cursor.fetchone()            
connection.commit()

"""
oldDate = datetime.datetime.now()
def postData2(roomCode, sensor_Id2,newDate):
    datax = {
            "Room_Id":roomCode,
            "Sensor_Id":sensor_Id2,
            "Alarm_Code":"true",
            "ReadDate_RaspPi":str(datetime.datetime.now()),
            "IsAlarmOn":"true"
            }
    return datax
def postData1(roomCode, sensor_Id1,list1,average1,MaxTemp,MinTemp,newDate):
    datax2 = {
	"Room_Code":roomCode,
        "Sensor_Id":sensor_Id1,
        "ReadCount":len(list1),
        "ReadAvg":average1,
        "ReadMax":MaxTemp,
        "ReadMin":MinTemp,
        "ReadDate_RaspPi":str(datetime.datetime.now())	
        }
    return datax2
        
headerxs = {'content-type': 'application/json','SecretKey' : 'H6Yv2nZZ3Hby3kwCNmPt4Rbxe8p5pA96'}

def Average(lst):
    return sum(lst) / len(lst)

while True:
    #read smoke
    #GPIO.setup(smokePin, GPIO.IN)
    #smokeOn = GPIO.input(smokePin)

    #read motion
    GPIO.setup(motionPin, GPIO.IN)
    motionOn = GPIO.input(motionPin)
    motionOn = GPIO.input(motionPin)
   
  
    #read temperature and humidity
    result = instance.read()
    result.is_valid
    newDate = datetime.datetime.now()
    
    if result.is_valid():
        print("Son okunma tarihi: " + str(datetime.datetime.now()))
        print("Sicaklik: %d C" % result.temperature)
        print("Nem: %d %%" % result.humidity)        
        if result.temperature > MaxTemp:
            MaxTemp = result.temperature
            print("MaxTemp = %d C" % MaxTemp)
        elif result.temperature < MinTemp:
            MinTemp = result.temperature
            print("MinTemp = %d C" % MinTemp)
        if result.humidity > MaxHum:
            MaxHum = result.humidity
            print("MaxHum = %d" % MaxHum)
        elif result.humidity < MinHum:
            MinHum = result.humidity
            print("MinHum = %d %%" % MinHum)
        if result.temperature > FromEmreMaxTemp or result.temperature < FromEmreMinTemp:
            postData2(roomCode, sensor_Id2,newDate)
            #try
            r = requests.post(url=AlarmAPIurl,data=json.dumps(postData2(roomCode, sensor_Id2,newDate)), headers= headerxs)
            pastebin_url= r.text
            print("The pastebin URL: %s \n"%pastebin_url)
        if result.humidity > FromEmreMaxHum or result.humidity < FromEmreMinTemp:
            postData2(roomCode, sensor_Id2,newDate)
            #try
            r = requests.post(url=AlarmAPIurl,data=json.dumps(postData2(roomCode, sensor_Id2,newDate)), headers= headerxs)
            pastebin_url= r.text
            print("The pastebin URL: %s \n"%pastebin_url)
        list1.append(result.temperature)
        #print(list1)
        list2.append(result.humidity)
        #print(list2)
        print(newDate.minute)
        print(oldDate.minute)
        average1 = Average(list1)
        average2 = Average(list2)        
    if (newDate - oldDate).seconds == 60:      
        #try except yazilacak
        postData1(roomCode, sensor_Id1,list1,average1,MaxTemp,MinTemp,newDate)
        r = requests.post(url=AlarmAPIurl,data=json.dumps(postData1(roomCode, sensor_Id1,list1,average1,MaxTemp,MinTemp,newDate)), headers= headerxs)
        pastebin_url= r.text
        postData1(roomCode, sensor_Id1,list1,average1,MaxTemp,MinTemp,newDate)
        #try except yazilacak isimleri duzelt
        try:
            if sensor_Type == "DI":
                if UnpostedDigitalData != Empty:
                    postAlertDigital = cursor.execute("SELECT * FROM UnpostedDigitalData")
                    for x in postAlertDigital: # olmadi burasi
                        postData2(roomCode, sensor_Id2,newDate)
                        r = requests.post(url=AlarmAPIurl,data=json.dumps(postData2(roomCode, sensor_Id2,newDate)), headers= headerxs)
                        pastebin_url= r.text
                        print("The pastebin URL: %s \n"%pastebin_url)
                        delete_UnpostedDigitalData = ("DELETE FROM * UnpostedDigitalData ")
                        cursor.execute(delete_UnpostedDigitalData)
                else:
                    r = requests.post(url=AlarmAPIurl,data=json.dumps(postData1(roomCode, sensor_Id1,list1,average1,MaxTemp,MinTemp,newDate)), headers= headerxs)
                    pastebin_url= r.text
                    print("The pastebin URL: %s \n"%pastebin_url)
            elif sensor_Type == "AI":
                if UnpostedAnalogData != Empty:
                    postAlertAnalog = cursor.execute("SELECT * FROM UnpostedAnalogData")
                    for x in postAlertAnalog:
                        postData1(roomCode, sensor_Id1,list1,average1,MaxTemp,MinTemp,newDate)
                        r = requests.post(url=AlarmAPIurl,data=json.dumps(postData1(roomCode, sensor_Id1,list1,average1,MaxTemp,MinTemp,newDate)), headers= headerxs)
                        pastebin_url= r.text
                        print("The pastebin URL: %s \n"%pastebin_url)
                        delete_UnpostedAnalogData = ("DELETE FROM * UnpostedDigitalData ")
                        cursor.execute(delete_UnpostedAnalogData)
                else:
                    r = requests.post(url=AlarmAPIurl,data=json.dumps(datax1), headers= headerxs)
                    pastebin_url= r.text
                    print("The pastebin URL: %s \n"%pastebin_url)
                
        except:
            """
            if sensor_Type == "DI":
                save_UnpostedDigitalData = ""INSERT INTO UnpostedDigitalData (UnpostedData_Id, Sensor_Id, RoomCode, AlarmCode, ReadDate_RaspPi, ExceptionCode) VALUES (%s, %s, %s, %s, %s, %s)""
                value = ("NULL",recordAlert[0], recordRoomId, recordRoomName, recordDevice[0], 'Read', datetime.datetime.now() ) # duzelt
                cursor.execute(save_UnpostedDigitalData, value)
                connection.commit()
            elif sensor_Type == "AI":
                save_UnpostedAnalogData = ""INSERT INTO UnpostedAnalogData (UnpostedAnalogData_Id, Sensor_Id, RoomCode, AlarmCode, ReadCount, ReadAverage,ReadMin, ReadMax, ReadDate_RaspPi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""
                value = ("NULL",recordAlert[0], recordRoomId, recordRoomName, recordDevice[0], 'Read', datetime.datetime.now() ) #duzelt
                cursor.execute(save_UnpostedAnalogData, value)
                connection.commit()
"""     

            
        oldDate = newDate
        del list1[ : ]
        print(list1)
        del list2[ : ]
        print(list2)          



"""        
        if tempHumUnreadCounter >= 10: 
            sqlquery = ""INSERT INTO ChangeOfReadStatus (changeOfReadStatus_Id, Alert_Code, Room_Id, Room_Name, Device_Id, Status, ReadDate) VALUES (%s, %s, %s, %s, %s, %s, %s )""        
            value = ("NULL",recordAlert[0], recordRoomId, recordRoomName, recordDevice[0], 'Read', datetime.datetime.now() )
            cursor.execute(sqlquery, value)
            connection.commit()
        tempHumUnreadCounter = 0
           
    else:
        print("okuma yapilamadi")
        tempHumUnreadCounter += 1

    if tempHumUnreadCounter  == 10:
        sql= ""INSERT INTO ChangeOfReadStatus (changeOfReadStatus_Id, Alert_Code, Room_Id, Room_Name, Device_Id, Status, ReadDate) VALUES (%s, %s, %s, %s, %s, %s, %s)""        
        valu= ("NULL",recordAlert[0], recordRoomId, recordRoomName, recordDevice[0], 'Unread', datetime.datetime.now())
        cursor.execute(sql, valu)
        print("dsadsad")
        connection.commit()
        print("dsadsad")
    time.sleep(1)
    """
time.sleep(1)
GPIO.cleanup()

