# Weather.py
# AI weather skill
# Kent Tran September 3rd, 2022

from pyowm import OWM
from geopy import Nominatim
from geopy import location
from datetime import datetime

class Weather():

    # The location of where you want to forecast for
    __location = "Waterloo, Canada"

    # API Key
    api_key = "c5709017c6cc0d9a982c93fe43e88bd9"

    def __init__(self):
        self.ow = OWM(self.api_key)
        self.mgr = self.ow.weather_manager()
        locator = Nominatim(user_agent="myGeocoder")
        city = "Waterloo"
        country = "Canada"
        self.__location = city + ", " + country
        loc = locator.geocode(self.__location)
        self.lat = loc.latitude
        self.long = loc.longitude

    @property
    def weather(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        return forecast

    @property
    def forecast(self):
        """ Returns the forecast at this location """

        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        detail_status = forecast.forecast_daily[0].detail_status
        pressure = str(forecast.forecast_daily[0].pressure.get('press'))
        humidity = str(forecast.forecast_daily[0].humidity)
        sunrise = datetime.utcfromtimestamp(forecast.forecast_daily[0].sunrise_time()).strftime("%H:%M:%S")
        sunset = datetime.utcfromtimestamp(forecast.forecast_daily[0].sunset_time()).strftime("%H:%M:%S")
        temperature = str(forecast.forecast_daily[0].temperature('celsius').get('day'))
        uvi = str(forecast.forecast_daily[0].uvi)
        
        # print the information of the details
        print("detailed status: ", detail_status)
        print("humidity: ", humidity)
        print("UVI ", uvi)
        print("Sunrise ", sunrise)
        print("Sunset ", sunset)
        print("Temperature ", temperature)
        print("UVI ", uvi)
        
        message = "Here is the weather: For today, the weather would be mostly " + detail_status \
                + ", humidity of " + humidity + " percent" \
                + " and a pressure of " + pressure + "millibars" \
                + ". Sunrise was at " + sunrise \
                + ". Sunset is at " + sunset \
                + ". " + uvi
        print(message)
        return message

# Demo:
myweather = Weather()
print(myweather.forecast)