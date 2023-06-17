import requests
from math import *

def distance(Lat1, Lat2, Lon1, Lon2):
    Lon1 = radians(Lon1)
    Lon2 = radians(Lon2)
    Lat1 = radians(Lat1)
    Lat2 = radians(Lat2)

    DLon = Lon2 - Lon1
    DLat = Lat2 - Lat1
    P = sin(DLat / 2) ** 2 + cos(Lat1) * cos(Lat2) * sin(DLon / 2) ** 2
    Q = 2 * asin(sqrt(P))
    R = 6371 # радиус земли

    return (Q * R)

ip1 = input('Введите IP(1): ')
ip2 = input('Введите IP(2): ')

r = requests.get(
    "http://ip-api.com/json/{}".format(
        ip1
    )
)

data = r.json()
rstatus = data['status']
rcountry = data['country']
rcity = data['city']
risp = data['isp']
Lat1 = data['lat']
Lon1 = data['lon']
      
r2 = requests.get(
    "http://ip-api.com/json/{}".format(
        ip2
    )
)
data2 = r2.json()
r2status = data2['status']
r2country = data2['country']
r2city = data2['city']
r2isp = data2['isp']
Lat2 = data2['lat']
Lon2 = data2['lon']

result = round(distance(Lat1, Lat2, Lon1, Lon2))

# '!=' - оператор неравенства
if ip1 != ip2:
    srawIps = '❗'
elif ip1 == ip2:
    srawIps = '✅'

if rcountry != r2country:
    srawCountrys = '❗'
elif rcountry == r2country:
    srawCountrys = '✅'

if rcity != r2city:
    srawCity = '❗'
elif rcity == r2city:
    srawCity = '✅'

if risp != r2isp:
    srawIsp = '❗'
elif risp == r2isp:
    srawIsp = '✅'

print(
    f'IP: {ip1} - {srawIps} - {ip2}\n'
    f'Страна: {rcountry} - {srawCountrys} - {r2country}\n'
    f'Город: {rcity} - {srawCity} - {r2city}\n'
    f'Провадер: {risp} - {srawIsp} - {r2isp}\n'
    f'Расстояние: {result} км\n'
)
