import requests

def weather(town):
    try:
        API_KEY = "0f29428662026b5e9bd47140e703469f"
        URL = "http://api.openweathermap.org/data/2.5/weather"
        parameters = {'q':town,'appid':API_KEY,'units':'metric','lang':'es'}
        response = requests.get(URL, params = parameters)
        # print(response.json())
        valueWeather = response.json()
        return show_request(valueWeather)
    except:
        print("Error")

def show_request(town):
    try:
        name_town = town['name']
        description_town = town['weather'][0]['description']
        temp_town = town['main']['temp']
        country_town = town['sys']['country']
        showTown = name_town
        showDescription = description_town
        showTemp  = str(int(temp_town)) + "°C"
        showCountry = country_town
        return {"showTown":showTown,"showDescription":showDescription,"showTemp":showTemp,"showCountry":showCountry}
    except:
        showTown = "Loading..."
        showDescription = "Try again"
        showTemp = ""
        showCountry = ""
        return {"showTown":showTown,"showDescription":showDescription,"showTemp":showTemp,"showCountry":showCountry}
