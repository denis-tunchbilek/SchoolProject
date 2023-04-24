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

    # Ищем ближайший магазин по заданным координатам
    params = {"apikey": API_KEY, "ll": f"{lon},{lat}", "type": "shop", "rspn": 1, "lang": "ru_RU"}
    response = requests.get("https://search-maps.yandex.ru/v1/", params=params)

    if response.status_code == 200:
        # Выводим информацию о ближайшем магазине
        result = response.json()["features"][0]
        print(result["properties"]["name"], result["properties"]["description"])
    else:
        print("Ошибка запроса к Яндекс.Поиску")
else:
    print("Ошибка запроса к Яндекс.Геокодеру")