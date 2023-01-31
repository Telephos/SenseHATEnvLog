#!/usr/bin/python3
#Trying to make this executable.
import mysql.connector as database
from sense_hat import SenseHat #sense hat 
import datetime #To get date and time
import os #to read path
from gpiozero import CPUTemperature #Getting cpu temp

sense = SenseHat()

#Pulling in the pressure, temp and humidity and formating it to one decimal place
pressure = sense.get_pressure()
pressure = '%.1f'%(pressure)
temp = sense.get_temperature()
temp = '%.1f'%(temp)
humidity = sense.get_humidity()
humidity = '%.1f'%(humidity)
cpuTemp = CPUTemperature().temperature
cpuTemp = '%.1f'%(cpuTemp)
normTemp = float(temp) - ((float(cpuTemp) - float(temp)) / 1.5) #have to cast as float type to work
fTempNorm = normTemp * (9/5) + 32
dateTime = datetime.datetime.now()

try:
    connection = database.connect(
        user="pi",
        password="enerJock9!7",
        host="localhost",
        database="env_data")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit()

cursor = connection.cursor()
cursor.execute("USE env_data;")
createDatabase = "CREATE TABLE IF NOT EXISTS senseHat(date_time DATETIME, pressure decimal(5,1), temp decimal(3,1), cpuTemp decimal(3,1), normTemp decimal(3,1), fTempNorm decimal(3,1), rh decimal(3,1));" 
cursor.execute(createDatabase)

def add_data(date_time, press, temper, cpuTemp, normTemp, fTemp, rh):
	try:
		statement = "INSERT INTO  senseHat (date_time,pressure,temp,cpuTemp,normTemp,fTempNorm,rh) VALUES (%s,%s,%s,%s,%s,%s,%s)"
		data = (date_time, press, temper, cpuTemp, normTemp, fTemp, rh)
		cursor.execute(statement, data)
		connection.commit()
		print("Successfully added entry to database.")
	except database.Error as e:
		print(f"Error adding entry to database: {e}")

add_data(dateTime,pressure,temp,cpuTemp,normTemp,fTempNorm,humidity)


