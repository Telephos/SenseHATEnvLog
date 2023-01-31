#!/usr/bin/python3
#Trying to make this executable.


from sense_hat import SenseHat #sense hat API
import csv #To write csv files
import datetime #To get date and time
import os #to read path

sense = SenseHat()

#Pulling in the ppressure, temp and humidity and formating it to one decimal place
pressure = sense.get_pressure()
pressure = '%.1f'%(pressure)
temp = sense.get_temperature()
temp = '%.1f'%(temp)
humidity = sense.get_humidity()
humidity = '%.1f'%(humidity)

x = datetime.datetime.now()
#print(x)

path = '/home/pi/workspace/sensehat/environmentsensors.csv'
file_exists = os.path.isfile(path) #Need this to check if the file exists

with open('environmentsensors.csv', 'a', newline='') as csvfile:
    fieldnames = ['time', 'pressure_millibars', 'temperature_celsius', 'humidity_rh']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader() #Only want to write the header once
        
    writer.writerow({'time': datetime.datetime.now(), 'pressure_millibars': pressure, 'temperature_celsius': temp, 'humidity_rh': humidity})

