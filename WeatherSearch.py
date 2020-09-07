import random
import re
import urllib.request

ip = input("Enter the Location : ")
url = "http://www.weather-forecast.com/locations/" + ip + "/forecasts/latest"
print(url)

data1 = urllib.request.urlopen(url).read()
# print(data1)
d = data1.decode("utf-8")
# print(d)
ans = re.search(
    'Pune (Mahārāshtra) Weather Forecast. Providing a local hourly Pune (Mahārāshtra) weather forecast of rain, sun, wind, humidity and temperature.',
    d)
# print(ans)
start = ans.start()
# print(start)

end = ans.end()
# print(end)
an = d[start:end]
print(an)
temp = random.randint(20, 30)
print(temp)
data3 = urllib.request.urlopen("https://api.thingspeak.com/update?api_key={key}&field1=" + str(temp))

print(data3)

if "Mostly dry" in an:
    data2 = urllib.request.urlopen("https://api.thingspeak.com/update?api_key={key}=" + str(1))
    print(data2)
elif "Light rains" in an:
    data2 = urllib.request.urlopen("https://api.thingspeak.com/update?api_key={key}=" + str(2))
    print(data2)
