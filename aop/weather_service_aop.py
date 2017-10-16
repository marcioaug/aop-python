class WeatherServiceAOP:

    def __init__(self):
        pass

    def check_wind(self, geo_place):
        return {
            'q': 'select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

    def check_condition(self, geo_place):
        return {
            'q': 'select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

    def check_sunset(self, geo_place):
        return {
            'q': 'select astronomy.sunset from weather.forecast where woeid in (select woeid from geo.places(1) where text = "' + geo_place + '")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

    def __str__(self):
        return "WeatherServiceAOP"

