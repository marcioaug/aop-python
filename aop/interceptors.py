import json
import urllib
import logging


from springpython.aop import MethodInterceptor

URL = 'https://query.yahooapis.com/v1/public/yql?'


class RequestInterceptor(MethodInterceptor):
    def invoke(self, invocation):
        return json.loads(
            urllib.urlopen(URL + urllib.urlencode(invocation.proceed())).read()
        )['query']['results']['channel']


class LoggingInterceptor(MethodInterceptor):
    def invoke(self, invocation):
        logging.warning('Call method %s for geo_place: %s', invocation.method_name, invocation.args[0])
        return invocation.proceed()