import logging

from springpython.aop import MethodInterceptor


class CacheInterceptor(MethodInterceptor):
    cache = {}

    def invoke(self, invocation):
        key = invocation.method_name + invocation.args[0]

        if key not in self.cache.keys():
            self.cache[key] = invocation.proceed()

        return self.cache[key]


class LoggingInterceptor(MethodInterceptor):
    def invoke(self, invocation):
        logging.warning('Call method %s for geo_place: %s', invocation.method_name, invocation.args[0])
        return invocation.proceed()