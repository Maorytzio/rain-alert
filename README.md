# rain-alert


This app is designed to retrieve weather data from the [OpenWeatherMap](https://openweathermap.org/api) API, which is a popular source for real-time weather information. The API provides access to a wide range of weather data, including temperature, humidity, wind speed, and precipitation. With this app, you can receive email alerts when it rains outside, reminding you to take an umbrella with you.

The app works by periodically querying the OpenWeatherMap API once a day via [python anywhere](https://www.pythonanywhere.com/) . checking the current weather conditions in your location. If it detects that it is currently raining, it will send an email notification to your designated email address, reminding you to take an umbrella before heading out.

