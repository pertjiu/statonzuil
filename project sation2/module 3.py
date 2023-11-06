import requests
import random

# Replace with your actual API key and latitude/longitude
api_key = "e8c04b8fe28cf2051ef9eb217735e859"


# Dictionary of city coordinates
city_coordinates = {
    "Arnhem": (51.9851, 5.8987),
    "Almere": (52.3508, 5.2645),
    "Amersfoort": (52.1561, 5.3878),
    "Almelo": (52.3566, 6.6626),
    "Alkmaar": (52.6324, 4.7537),
    "Apeldoorn": (52.2112, 5.9699),
    "Assen": (52.9913, 6.5645),
    "Amsterdam": (52.3676, 4.9041),
    "Boxtel": (51.5792, 5.3192),
    "Breda": (51.5867, 4.7755),
    "Dordrecht": (51.8134, 4.6909),
    "Delft": (52.0116, 4.3571),
    "Deventer": (52.2518, 6.1561),
    "Enschede": (52.2200, 6.8951),
    "Gouda": (52.0168, 4.7105),
    "Groningen": (53.2194, 6.5665),
    "Den Haag": (52.0705, 4.3007),
    "Hengelo": (52.2670, 6.7930),
    "Haarlem": (52.3874, 4.6462),
    "Helmond": (51.4795, 5.6614),
    "Hoorn": (52.6420, 5.0600),
    "Heerlen": (50.8845, 5.9793),
    "Den Bosch": (51.6998, 5.3041),
    "Hilversum": (52.2272, 5.1694),
    "Leiden": (52.1601, 4.4970),
    "Lelystad": (52.5185, 5.4714),
    "Leeuwarden": (53.2012, 5.7999),
    "Maastricht": (50.8503, 5.6880),
    "Nijmegen": (51.8126, 5.8372),
    "Oss": (51.7653, 5.5273),
    "Roermond": (51.1942, 6.0105),
    "Roosendaal": (51.5303, 4.4577),
    "Sittard": (51.0028, 5.8694),
    "Tilburg": (51.5555, 5.0910),
    "Utrecht": (52.0907, 5.1214),
    "Venlo": (51.3704, 6.1722),
    "Vlissingen": (51.4416, 3.5734),
    "Zaandam": (52.4404, 4.8104),
    "Zwolle": (52.5168, 6.0835),
    "Zutphen": (52.1394, 6.1962)
}



selected_city = random.choice(list(city_coordinates.keys()))

# Get the latitude and longitude for the selected city
latitude, longitude = city_coordinates[selected_city]

# Build the API request URL
resource_uri = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

# Make the API request
response = requests.get(resource_uri)
response_data = response.json()

print(f"Weather data for {selected_city}:")
print(response_data)



