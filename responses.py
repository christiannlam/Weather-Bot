from discord import user
import weather

#Bot Commands
def handle_response(message):
  userMsg = message.lower()
  location = list(userMsg.split(" "))
  
  if location[0] == 'weather':
    if len(location) == 4:
      city = str(location[1]) + str(location[2])
      weather.getCords(city,location[3])
      return weather.getWeather()
    elif len(location) == 3:
      weather.getCords(location[1],location[2])
      return weather.getWeather()
    else:
      return "Invalid City / State"