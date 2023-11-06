import os
from datetime import datetime
import requests
import psycopg2
from tkinter import *
import random
from PIL import Image, ImageTk

icon_directory = r"C:\Users\dunca\PycharmProjects\final-assignment\icons"
api_key = "e8c04b8fe28cf2051ef9eb217735e859"



# Function to get station info
def get_station_info():
    with open("stations.txt", "r") as file:
        content = file.read()
        wordlist = content.split()
        station = random.choice(wordlist)

    conn = psycopg2.connect(
        host="20.77.182.19",
        database='stationszuil',
        user='postgres',
        password="FD1ns81g02!!"
    )
    cursor = conn.cursor()

    query = "SELECT * FROM station_service WHERE station_city = %s;"
    cursor.execute(query, (station,))
    stationinfo = cursor.fetchall()

    facilities = []

    facility_names = {
        True: "available",
        False: "not available",
    }

    for serve in stationinfo:
        facility_2 = facility_names.get(serve[2], "unknown")
        facility_3 = facility_names.get(serve[3], "unknown")
        facility_4 = facility_names.get(serve[4], "unknown")
        facility_5 = facility_names.get(serve[5], "unknown")

        if facility_2 == "not available":
            pass
        else:
            facilities.append("OV-BIKE")
        if facility_3 == "not available":
            pass
        else:
            facilities.append("ELEVATOR")
        if facility_4 == "not available":
            pass
        else:
            facilities.append("TOILETS")
        if facility_5 == "not available":
            pass
        else:
            facilities.append("PARK_AND_RIDE")

    helpt = []

    if facilities:
        st = f"{station} {serve[1]}:"
        helpt = [facility for facility in facilities]
        helpt_str = ', '.join(helpt)
        helpt_str = helpt_str.replace("[", "").replace("]", "").replace("'", "").replace(",", "")

        return f"{st}\n{helpt_str}"


    conn.close()

# At the beginning of your program, to initialize the station info
get_station_info()

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

weather_icons = {
    "thunderstorm with light rain": "11d@2x.png",
    "thunderstorm with rain": "11d@2x.png",
    "thunderstorm with heavy rain": "11d@2x.png",
    "light thunderstorm": "11d@2x.png",
    "thunderstorm": "11d@2x.png",
    "heavy thunderstorm": "11d@2x.png",
    "ragged thunderstorm": "11d@2x.png",
    "thunderstorm with light drizzle": "11d@2x.png",
    "thunderstorm with drizzle": "11d@2x.png",
    "thunderstorm with heavy drizzle": "11d@2x.png",
    "light intensity drizzle": "09d@2x.png",
    "drizzle": "09d@2x.png",
    "heavy intensity drizzle": "09d@2x.png",
    "light intensity drizzle rain": "09d@2x.png",
    "drizzle rain": "09d@2x.png",
    "heavy intensity drizzle rain": "09d@2x.png",
    "shower rain and drizzle": "09d@2x.png",
    "heavy shower rain and drizzle": "09d@2x.png",
    "shower drizzle": "09d@2x.png",
    "light rain": "10d@2x.png",
    "moderate rain": "10d@2x.png",
    "heavy intensity rain": "10d@2x.png",
    "very heavy rain": "10d@2x.png",
    "extreme rain": "10d@2x.png",
    "freezing rain": "13d@2x.png",
    "light intensity shower rain": "09d@2x.png",
    "shower rain": "09d@2x.png",
    "heavy intensity shower rain": "09d@2x.png",
    "ragged shower rain": "09d@2x.png",
    "light snow": "13d@2x.png",
    "snow": "13d@2x.png",
    "heavy snow": "13d@2x.png",
    "sleet": "13d@2x.png",
    "light shower sleet": "13d@2x.png",
    "shower sleet": "13d@2x.png",
    "light rain and snow": "13d@2x.png",
    "rain and snow": "13d@2x.png",
    "light shower snow": "13d@2x.png",
    "shower snow": "13d@2x.png",
    "heavy shower snow": "13d@2x.png",
    "mist": "50d@2x.png",
    "smoke": "50d@2x.png",
    "haze": "50d@2x.png",
    "sand/dust whirls": "50d@2x.png",
    "fog": "50d@2x.png",
    "sand": "50d@2x.png",
    "dust": "50d@2x.png",
    "volcanic ash": "50d@2x.png",
    "squalls": "50d@2x.png",
    "tornado": "50d@2x.png",
    "clear sky": "01d@2x.png",
    "few clouds": "02d@2x.png",
    "scattered clouds": "03d@2x.png",
    "broken clouds": "04d@2x.png",
    "overcast clouds": "04d@2x.png"
}

conn = psycopg2.connect(
    host="20.77.182.19",
    database='stationszuil',
    user='postgres',
    password="FD1ns81g02!!"
)
cursor = conn.cursor()

query = """SELECT bericht
           FROM bericht
           ORDER BY bericht_id DESC
           LIMIT 5;"""
cursor.execute(query)
bericht_rows = cursor.fetchall()

with open("stations.txt", "r") as file:
    content = file.read()
    wordlist = content.split()
    station = random.choice(wordlist)

query = """SELECT *
           FROM station_service
           WHERE station_city = %s;"""
cursor.execute(query, (station,))
stationinfo = cursor.fetchall()

conn.close()


def get_3_hourly_forecast():
    selected_city = station(list(city_coordinates.keys()))
    latitude, longitude = city_coordinates[selected_city]

    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    weather_info_frame = Frame(weather_frame, background='#FFFFFF')
    weather_info_frame.pack()

    for entry in forecast_data['list'][:5]:
        timestamp = datetime.utcfromtimestamp(entry['dt']).strftime('%T')
        temperature_kelvin = entry['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        description = entry['weather'][0]['description']

        icon_filename = weather_icons.get(description, "default@2x.png")

        icon_path = os.path.join(icon_directory, icon_filename)
        icon_image = Image.open(icon_path)
        icon_image = ImageTk.PhotoImage(icon_image)

        icon_label = Label(weather_info_frame, image=icon_image)
        icon_label.image = icon_image
        icon_label.pack(side=LEFT, padx=10)


        weather_label = Label(weather_info_frame, text=f"{timestamp}: {description}, {temperature_celsius:.2f}°C",
                              font=('NS Sans Regular', 14), foreground='#003082', background='#FFFFFF')
        weather_label.pack(side=LEFT)

    return


root = Tk()
root.geometry("1600x1300")
root.attributes('-fullscreen', True)
root.configure(background='#003082')


station_bericht_frame = Frame(root, background='#E6E6E9')
station_bericht_frame.grid(row=0, column=0, padx=450, pady= 20)


station_label = Label(station_bericht_frame, text=f"Station: {station}", font=('NS Sans Regular', 20), foreground='#0063D3', background='#E6E6E9')
station_label.grid(row=0, column=0, pady=0)
station_label_info = Label(station_bericht_frame, text=f" {get_station_info()}", font=('NS Sans Regular', 20), foreground='#0063D3', background='#E6E6E9')
station_label_info.grid(row=0, column=0, pady=0)
bericht_label = Label(station_bericht_frame, text="Latest Messages:", font=('NS Sans Regular', 20), foreground='#0063D3', background='#E6E6E9')
bericht_label.grid(row=1, column=0, pady=10)

row = 2

for row, bericht_row in enumerate(bericht_rows, start=row):
    bericht_item = Label(station_bericht_frame, text=bericht_row[0], font=('NS Sans Regular', 14), foreground='#0063D3', background='#E6E6E9')
    bericht_item.grid(row=row, column=0, pady=50)

station_bericht_frame = Frame(root, background='#FFC917')
station_bericht_frame.grid(row=0, column=0, padx=20, pady=20)


weather_frame = Frame(root, background='#FFC917')
weather_frame.grid(row=1, column=0, padx=3, pady=20, sticky="ew")


weather_horizontal_frame = Frame(weather_frame, background='#FFC917')
weather_horizontal_frame.grid(row=1, column=2, padx=600, pady=10, sticky="ew")
def display_weather_forecast():
    selected_city = random.choice(list(city_coordinates.keys()))
    latitude, longitude = city_coordinates[selected_city]

    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    for entry in forecast_data['list'][:5]:
        timestamp = datetime.utcfromtimestamp(entry['dt']).strftime('%T')
        temperature_kelvin = entry['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        description = entry['weather'][0]['description']

        icon_filename = weather_icons.get(description)

        icon_path = os.path.join(icon_directory, icon_filename)

        original_icon = Image.open(icon_path).convert("RGBA")

        new_image = Image.new("RGBA", original_icon.size, ("#003082"))

        new_image.paste(original_icon, (0, 0), original_icon)

        icon_image = ImageTk.PhotoImage(new_image)

        icon_label = Label(weather_horizontal_frame, image=icon_image)
        icon_label.image = icon_image
        icon_label.grid(row=0, column=len(weather_horizontal_frame.winfo_children()), padx=10)

        time_temp_frame = Frame(weather_horizontal_frame, background='#FFFFFF')
        time_temp_frame.grid(row=1, column=len(weather_horizontal_frame.winfo_children()) - 1, padx=10)

        time_label = Label(time_temp_frame, text=timestamp, font=('NS Sans Regular', 14), foreground='#0063D3', background='#FFC917')
        time_label.grid(row=0, column=0)

        temp_label = Label(time_temp_frame, text=f"{temperature_celsius:.2f}°C", font=('NS Sans Regular', 14), foreground='#0063D3', background='#FFC917')
        temp_label.grid(row=0, column=1)

display_weather_forecast()

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()

#netter maken nog

