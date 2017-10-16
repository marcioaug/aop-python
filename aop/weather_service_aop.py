import json
import urllib

class WeatherServiceAOP:

    def __init__(self):
        self.url = 'https://query.yahooapis.com/v1/public/yql?'

    def request(self, query):
        result = urllib.urlopen(self.url + urllib.urlencode(query)).read()
        return json.loads(result)['query']['results']['channel']

    def check_wind(self, geo_place):
        query = {
            'q': 'select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

        return self.request(query)

    def check_condition(self, geo_place):
        query = {
            'q': 'select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

        return self.request(query)

    def check_sunset(self, geo_place):
        query = {
            'q': 'select astronomy.sunset from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

        return self.request(query)

    def __str__(self):
        return "WeatherServiceAOP"

