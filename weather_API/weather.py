import requests

"""
This project is about requesting a weather API key and use it to retrieve weather decscription and temperature data for any requested city.
to use it:
run the file, type a city name, get data.

"""

# this API was taken from a weather website -> https://openweathermap.org/current
API_KEY = "bef28bda6117928f24255ad0672bf1bd"

# to define where are we sending the request to, you can find this when you choose to call an api of the same website
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# get the city for the weather data
city = input("Enter a city name: ")

# build a url that contains the city and the API key to be able to send the request
# after ? is a query parameter --> the API key that i want to pass
# q is another parameter (query), to look for the data of the required city
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#make a get HTTP request method to get the data back
response = requests.get(request_url)

#check if everything is right
# if response.status_code == 200:
#     # will give json data as python dictonary
#     data = response.json()
#     print(data)
# else:
#     print("Error found")


# now if you run the code, you will add a city name then it will show you a dictionary of the API data associated with that city
# we want to access specific data: weather and tempreture...
# to do that i need to access some keys and their values
if response.status_code == 200:
    data = response.json()
    #to access the element in the dictionary in the list
    weather = data["weather"][0]["description"]
    print(f"Weather description in {city}: {weather}")

    temperature = data["main"]["temp"]
    # to convert temperature from Kalvin to celsius, and round it to nearest 2 decimels
    temp = round(temperature - 273, 2)
    print(f"Temperature in {city} is {temp} Celsius")

else:
    print("Error found")
