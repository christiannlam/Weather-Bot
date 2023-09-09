import os, urllib.request, json, time


#Storing API Key in "Secrets" since unable to create ENV file
API = os.environ["APIKEY"]
API_URL = 'http://api.weatherstack.com/current?'
API_URL += 'access_key=' + API
API_URL += '&query=33.669445,-117.823059'

def get_temp(celcius):
  return (celcius * 9/5) + 32
  
def main():
  #Requesting data from API and decoding
  request = urllib.request.Request(API_URL)
  response = urllib.request.urlopen(request).read().decode()
  
  #Reads json data into python data
  data = json.loads(response)
  
  #Parsing data for City,Country,Time,Temperature
  city = data["location"]["name"]
  country = data["location"]["country"]
  currentTime = data["location"]["localtime"]
  temperature = data["current"]["temperature"]

  #Return Info
  print(f"Location: {city}, {country}\nTime: {currentTime}\nTemperature: {get_temp(temperature)}")
  time.sleep(60)

if __name__ == "__main__":
  main()
  


  