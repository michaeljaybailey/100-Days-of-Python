import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

apikey = os.environ.get("OWM_KEY")
account_sid = "AC99678bd2487ebb862a29b2f17f539ace"
auth_token = os.environ.get("AUTH_TOKEN")

MY_LATITUDE = 34.36
MY_LONGITUDE = -118.38

weather_params = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": apikey,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=weather_params)
response.raise_for_status()
data = response.json()

weather_slice = data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It is going to rain, bring an umbrella.",
        from_="+18594848536",
        to="+16613105457"
    )
    print(message.status)


