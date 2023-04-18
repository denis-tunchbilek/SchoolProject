from geopy import GoogleV3


place = "улица Твардовского д.12 к3 Москва"
location = GoogleV3().geocode(place)