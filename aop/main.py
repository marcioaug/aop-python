from springpython.config import PythonConfig, Object
from springpython.context import ApplicationContext, scope
from springpython.aop import ProxyFactoryObject, RegexpMethodPointcutAdvisor

from weather_service import WeatherService
from weather_service_aop import WeatherServiceAOP
from interceptors import CacheInterceptor, LoggingInterceptor


class ExampleApplicationContext(PythonConfig):
    def __init__(self):
        super(ExampleApplicationContext, self).__init__()

    def target_weather_service(self):
        return WeatherServiceAOP()

    @Object(scope.SINGLETON)
    def weather_service(self):
        pointcut_advisor = RegexpMethodPointcutAdvisor(
            advice=[
                LoggingInterceptor(),
                CacheInterceptor()
            ],
            patterns=[".*check_.*"]
        )

        return ProxyFactoryObject(
            target=self.target_weather_service(),
            interceptors=[pointcut_advisor]
        )


def main():
    container = ApplicationContext(ExampleApplicationContext())

    weather_service = WeatherService()
    geo_place = 'Maceio, AL'
    wind = weather_service.check_wind(geo_place)
    condition = weather_service.check_condition(geo_place)
    sunset = weather_service.check_sunset(geo_place)

    print('Direction: %s' % wind['wind']['direction'])
    print('Speed: %s' % wind['wind']['speed'])
    print('Condition: %s' % condition['item']['condition']['text'])
    print('Sunset: %s' % sunset['astronomy']['sunset'])

    weather_service = container.get_object('weather_service')
    geo_place = 'Maceio, AL'
    wind = weather_service.check_wind(geo_place)
    condition = weather_service.check_condition(geo_place)
    sunset = weather_service.check_sunset(geo_place)

    print('====== AOP ======')
    print('Direction: %s' % wind['wind']['direction'])
    print('Speed: %s' % wind['wind']['speed'])
    print('Condition: %s' % condition['item']['condition']['text'])
    print('Sunset: %s' % sunset['astronomy']['sunset'])


if __name__ == '__main__':
    main()