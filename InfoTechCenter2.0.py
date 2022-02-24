import random

#Weather Branch

def weatherList():
    weatherForecast =["Snow", "Ice", "Heavy Rain", "Windy", "Foggy", "Sunny",]
    weatherRandom = random.choice(weatherForecast)
    return weatherRandom
#Calling weather function for obvious reasons
weatherAlert = weatherList()

def VRS():
    if weatherAlert == "Ice":
        print("\nVRS has changed your alarm 30 minutes early based on NWS reports of", weatherAlert)
        print("VRS will only allow your car to go 30 MPH")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your alarm 15 minutes early based on NWS reports of", weatherAlert)
        print("VRS will only allow your car to go 50 MPH")
    elif weatherAlert == "Heavy Rain":
        print("\nVRS has changed your alarm 60 minutes early based on NWS reports of", weatherAlert)
        print("VRS will only allow your car to go 30 MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your alarm 30 minutes early based on NWS reports of", weatherAlert)
        print("VRS will only allow your car to go 60 MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your alarm 20 minutes early based on NWS reports of", weatherAlert)
        print("VRS will only allow your car to go 35 MPH")
    elif weatherAlert == "Sunny":
        print("\nVRS has not changed your alarm based on NWS reports of", weatherAlert)
        print("VRS will allow your car to go up to 120 MPH")
print(VRS())