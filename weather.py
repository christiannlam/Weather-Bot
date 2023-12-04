import os, urllib.request, json, time
import cords

#Storing API Key in "Secrets" since unable to create ENV file
API_Weather = os.environ["APIKEY"]
API_GEO = os.environ["Geo_Key"]

cords = cords.Cords()

def getCords(city, state):
  
  GEO_URL = 'https://api.geoapify.com/v1/geocode/search?'
  GEO_URL += 'city=' + city
  GEO_URL += '&state=' + state
  GEO_URL += '&apiKey=' + API_GEO
  print(GEO_URL)
  request = urllib.request.Request(GEO_URL)
  response = urllib.request.urlopen(request).read().decode()
  
  data = json.loads(response)
  
  cords.set_lat(data["features"][0]["properties"]["lat"])
  cords.set_lon(data["features"][0]["properties"]["lon"])
  
def getTemp(celcius):
  return (celcius * 9/5) + 32
  
def getWeather():
  WEATHER_URL = 'http://api.weatherstack.com/current?'
  WEATHER_URL += 'access_key=' + API_Weather
  WEATHER_URL += f"&query={cords.get_lat()},{cords.get_lon()}"
  print(WEATHER_URL)
  #Requesting data from API and decoding
  request = urllib.request.Request(WEATHER_URL)
  response = urllib.request.urlopen(request).read().decode()
  
  #Reads json data into python data
  data = json.loads(response)
  
  #Parsing data for City,Country,Time,Temperature
  city = data["location"]["name"]
  country = data["location"]["country"]
  currentTime = data["location"]["localtime"]
  temperature = data["current"]["temperature"]

  #Return Info
  return str(f"Location: {city}, {country}\nTime: {currentTime}\nTemperature: {getTemp(temperature)} Degrees Farenheit")
  time.sleep(60)

  


  