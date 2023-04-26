import  requests

API_KEY = "deebbc39-ebe1-480f-924a-a572509479c2"
address = "Москва, Красная площадь"

# Запрос на обратное геокодирование, чтобы получить координаты адреса
params = {"apikey": API_KEY, "geocode": address, "format": "json"}
response = requests.get("https://geocode-maps.yandex.ru/1.x/", params=params)

if response.status_code == 200:
    # Получаем координаты из ответа метода "обратного геокодирования"
    pos = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = map(float, pos.split())
re = requests.get("https://catalog.api.2gis.com/3.0/items?q=кафе&type=branch&point=37.416469%2C55.619325&radius=1000&key=rukpgh0564")
print(re.json())