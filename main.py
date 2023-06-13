import requests
import smtplib
import os

LAT = "45.323020"
LNG = "23.094370"
api_key = os.environ.get("OWM_API_KEY")
OWM_endpoint = "https://api.openweathermap.org/data/2.8/onecall"

params = {
    "lat": LAT,
    "lon": LNG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=params)
twelve_hours_forecast = response.json()["hourly"][:12]

is_rain = False
for forecast in twelve_hours_forecast:
    weather_id = forecast["weather"][0]["id"]
    if weather_id < 700:
        is_rain = True

if is_rain:
    my_email = "ttestar459@gmail.com"
    password = "mbfmvdswcytedgox"
    recipient = "teast2test2@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # make connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:Weather Alert!\n\nHello,\nDont forget your umbrella!\t\t\t")

    print("Rain ☔")
