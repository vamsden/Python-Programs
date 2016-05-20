# Weather Parsing
import requests
from bs4 import BeautifulSoup

data = requests.get(
    "http://www.accuweather.com/en/in/panaji/188095/weather-forecast/188095")

# To print data use --> data.text
soup = BeautifulSoup(data.text, "html.parser")

# Note: Fahrenheits were conerted to degrees
data2 = soup.find('div', {'class': 'info'}, {'class': 'cond'})
data3 = soup.find('strong', {'class': 'temp'})
temp = data3.contents[0]

print("Current temperature in Panaji is: " + temp + " degrees")
