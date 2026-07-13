import requests


def get_weather(location):

    """
    Gets current weather data.
    """

    # Example coordinates
    # Later we can make location -> coordinates automatically

    coordinates = {
        "Ilorin": {
            "lat": 8.4966,
            "lon": 4.5421
        },

        "Lagos": {
            "lat": 6.5244,
            "lon": 3.3792
        },

        "Kwara": {
            "lat": 8.9669,
            "lon": 4.3874
        }
    }


    place = coordinates.get(
        location,
        coordinates["Ilorin"]
    )


    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={place['lat']}"
        f"&longitude={place['lon']}"
        "&current=temperature_2m,relative_humidity_2m,rain"
    )


    response = requests.get(url)

    data = response.json()


    current = data["current"]


    return {

        "temperature":
        f"{current['temperature_2m']}°C",


        "humidity":
        f"{current['relative_humidity_2m']}%",


        "rainfall":
        f"{current['rain']} mm",


        "condition":
        "Current weather"

    }