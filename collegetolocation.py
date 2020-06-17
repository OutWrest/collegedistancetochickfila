import csv 
from geopy.geocoders import Nominatim
from time import sleep

filename = "Colleges.csv"
geolocator = Nominatim(user_agent="chikfila")

colleges = []
locations = []

with open(filename, 'r', encoding="utf8") as csvfile: 
    csvreader = csv.reader(csvfile) 
    
    fields = next(csvreader) 
  
    for row in csvreader: 
        colleges.append([row[2], row[3]]) 
        
with open('colleges_locations2.txt', 'w') as f:
    for i, college in enumerate(colleges):
        sleep(2)
        
        name, address = college
        location = geolocator.geocode(address, timeout=60)
        
        try:
            locations.append([name, (location.latitude, location.longitude)])
        except:
            continue

        print((i/7150)*100, (location.latitude, location.longitude))
        
        f.write("{}:{}\n".format(name, location[1]))