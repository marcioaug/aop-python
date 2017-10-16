import logging
import json
import urllib


class WeatherService:

    def __init__(self):
        self.url = 'https://query.yahooapis.com/v1/public/yql?'

    def check_wind(self, geo_place):
        logging.warning('Call method check_wind for geo_place: %s', geo_place)

        query = {
            'q': 'select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

        result = urllib.urlopen(self.url + urllib.urlencode(query)).read()
        return json.loads(result)['query']['results']['channel']

    def check_condition(self, geo_place):
        logging.warning('Call method check_condition for geo_place: %s', geo_place)

        query = {
            'q': 'select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

        result = urllib.urlopen(self.url + urllib.urlencode(query)).read()
        return json.loads(result)['query']['results']['channel']

    def check_sunset(self, geo_place):
        logging.warning('Call method check_sunset for geo_place: %s', geo_place)

        query = {
            'q': 'select astronomy.sunset from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

        result = urllib.urlopen(self.url + urllib.urlencode(query)).read()
        return json.loads(result)['query']['results']['channel']
