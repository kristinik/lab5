from enum import Enum

class WeatherType(Enum):
    SUNNY = "Sunny"
    CLOUDY = "Cloudy"
    RAINY = "Rainy"
    FOGGY = "Foggy"

class Weather:
      def __init__(self, day, city, country, temp, humidity, wind_speed, weather_type):
        self.day = day
        self.city = city
        self.country = country
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.weather_type = weather_type

class WeatherCalendar:
    def __init__(self):
        self.weather_entries = []

    def add_weather_entry(self, weather_entry):
        self.weather_entries.append(weather_entry)

    def find_max_temperature(self, day):
        temperatures = [weather.temp for weather in self.weather_entries if weather.day == day]
        if not temperatures:
            return "Not enough data"
        return max(temperatures)

    def is_lviv_weather(self, humidity, weather_type):
        if humidity > 80 and weather_type == WeatherType.RAINY:
            return "The typical day in Lviv"
        else:
            return "You're lucky, man"

    def sort_weather_entries_by_day(self):
        self.weather_entries.sort(key=lambda x: x.day)

# Приклад використання
if __name__ == "__main__":
    weather_entry1 = Weather(day="2023-11-13", city="Lviv", country="Ukraine", temp=20, humidity=75, wind_speed=10, weather_type=WeatherType.SUNNY)
    weather_entry2 = Weather(day="2023-11-13", city="Lviv", country="Ukraine", temp=18, humidity=85, wind_speed=8, weather_type=WeatherType.RAINY)
    weather_entry3 = Weather(day="2023-11-14", city="Lviv", country="Ukraine", temp=22, humidity=70, wind_speed=12, weather_type=WeatherType.CLOUDY)

    weather_calendar = WeatherCalendar()
    weather_calendar.add_weather_entry(weather_entry1)
    weather_calendar.add_weather_entry(weather_entry2)
    weather_calendar.add_weather_entry(weather_entry3)

    max_temp = weather_calendar.find_max_temperature(day="2023-11-13")
    print(f"Max temperature on 2023-11-13: {max_temp}")

    prediction = weather_calendar.is_lviv_weather(humidity=85, weather_type=WeatherType.RAINY)
    print(prediction)

    weather_calendar.sort_weather_entries_by_day()
    for entry in weather_calendar.weather_entries:
        print(f"{entry.day}: {entry.temp}°C, {entry.weather_type.value}")
