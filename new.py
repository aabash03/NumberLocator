import phonenumbers
from phonenumbers import geocoder
from test import number
import folium

key = "5af6785801934a7fb14b16cd6c12add8"

check_number = phonenumbers.parse(number)
location = geocoder.description_for_number(check_number,"en")
print("Country: ",location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print("Service Provider: ",carrier.name_for_number(service_provider, "en"))


from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print("Latitude:",lat,"\n","Longitude: ",lng)


map_location = folium.Map(location = [lat,lng], zoom_start = 9)
folium.Marker([lat,lng],popup = location).add_to(map_location)
map_location.save("mylocation.html")