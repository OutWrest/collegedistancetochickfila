from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim(user_agent="chikfilav2")

with open('every_chickfila_in_the_country.txt', 'r', encoding='utf8') as f:
    chikfilas = [a.split(':') for a in f.read().splitlines()]
    #print(chikfilas)
    with open('chickfila_locations2.txt', 'w') as o:
        i = 0

        for state, name, address in chikfilas:
            sleep(1.2)

            location = geolocator.geocode(address, timeout=5)

            try:
                print((i/7150)*100, (location.latitude, location.longitude))
            except:
                continue

            o.write("{}:{}\n".format(name, location[1]))
            i+=1