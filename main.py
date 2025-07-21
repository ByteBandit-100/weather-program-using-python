import requests

def search_details():
    location = data['name']
    w_status = data['weather'][0]['description']
    temp = f'{(data['main']['temp'] - 273.15):.2f} °C'
    humi = f'{data['main']['humidity']} % '
    wi_speed = f'{data['wind']['gust']} meter/second'
    cloud = f'{data['clouds']['all']} %'
    return location,w_status,temp,humi,wi_speed,cloud

status = {
    "scattered clouds" : "☁",
    "broken clouds" : "☁",
    "overcast clouds" :  "☁",
    "few clouds" :  "☁",
    "light rain" : "☔",
    "heavy rain" : "⛈️",
    "clear sky"  : "🌞",
    "snow":"❄️"
}

while True:
    print('X--------------------- Search Weather ---------------------X\n')

    city_name = input('Enter city or q for quit : ').lower()
    if city_name == 'q':
        break
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=259af413e4e878a10cf624c77ab5e67c'
    r = None
    try:
        r = requests.get(url)
        data = r.json()
        if r.status_code == 200:
            location_name, weather_status, temperature, humidity, wind_speed, clouds = search_details()
            print(f'\n{'Location'.ljust(15)} : {location_name}')
            print(f'{'Weather status'.ljust(15)} : {weather_status} {status[weather_status]}')
            print(f'{'Temperature'.ljust(15)} : {temperature}')
            print(f'{'Humidity'.ljust(15)} : {humidity} 💧')
            print(f'{'Wind Speed'.ljust(15)} : {wind_speed} 〰️〰️')
            print(f'{'Clouds'.ljust(15)} : {clouds}\n')

        elif r.status_code >= 400 :
            print(f'\nNo Data Found 🧐\nTry again.\n')
    except:
        print("\n⚠️ No Internet Connection ⚠️\n")