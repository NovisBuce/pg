# Příklad 2: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `fetch_weather_data`, která:
# 1. Přijme jako parametr město (`city`), s tímto městem a klíčem `api_key` získejte aktuální teplotu z url `http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}`.
# 2. Teplota je uložená v slovníku `main` pod klíčem `temp` v Kelvinech.
# 3. Funkce vrátí teplotu v °C zaokrouhlenou na dvě desetinná místa (273.15 °K = 0 °C).


import requests


# API klíč pro OpenWeatherMap
api_key = 'a023a3be26e530f37924110734b494b1'


def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try: 
        response = requests.get(url)

    


# Unit testy
from unittest.mock import patch, MagicMock

def test_fetch_weather_data():
    mock_response = {
        "main": {
            "temp": 293.15  # Teplota v Kelvinech
        }
    }
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_response))
        assert fetch_weather_data("Prague") == 20.0  # 293.15 K = 20.0 °C


if __name__ == "__main__":
    city = input("Enter city name: ")
    temperature = fetch_weather_data(city)
    print(f"Current temperature in {city}: {temperature} °C")