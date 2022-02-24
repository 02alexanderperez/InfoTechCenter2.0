import random

#Weather Branch

def weatherList():
    weatherForecast =["Snow", "Ice", "Heavy Rain", "Windy", "Foggy", "Sunny", "clear"]
    weatherRandom = random.choice(weatherForecast)
    return weatherRandom
#Calling weather function for obvious reasons
weatherAlert = weatherList()













