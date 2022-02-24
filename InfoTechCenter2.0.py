import random

#Weather Branch

def weatherList():
    weatherForecast =["Snow", "Ice", "Heavy Rain", "Windy", "Foggy", "Sunny", "clear"]
    weatherRandom = random.choice(weatherForecast)
    return weatherRandom
#Calling weather function for obvious reasons
weatherAlert = weatherList()

def VRS():
     if weatherAlert == "Ice":
         print("\nVRS has changed your alarm 30 minutes early based on NWS reports of",weatherAlert)
         print("VRS will only allow your car to go 30 MPH")


vehicleResponseSystem():











