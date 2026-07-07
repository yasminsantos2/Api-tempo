import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def buscar_clima(cidade):
    """Busca o clima de uma cidade e devolve os dados já organizados."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br",
    }

    resposta = requests.get(url, params=parametros)
    dados = resposta.json()

    return {
        "cidade": cidade,
        "temperatura": dados["main"]["temp"],
        "sensacao": dados["main"]["feels_like"],
        "umidade": dados["main"]["humidity"],
        "descricao": dados["weather"][0]["description"],
    }
