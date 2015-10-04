# -*- coding: utf-8 -*-

import requests
import logging
import sys

from apiwrapper import APIWrapper

API_URL = 'https://api.sandbox.amadeus.com/v1.2'


def configure_logger(log_level=logging.WARN):
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    try:
        sa = logging.StreamHandler(stream=sys.stdout)
    except TypeError:
        sa = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
    sa.setFormatter(formatter)
    logger.addHandler(sa)
    return logger

log = configure_logger()
STRICT, GRACEFUL, IGNORE = 'strict', 'graceful', 'ignore'


class Transport(APIWrapper):

    def __init__(self, api_key, api_url=API_URL):
        if not api_key:
            log.warning("API Key is not set.")
        self.api_key = api_key
        self.api_url = api_url

    def make_request(self, service_url, method='get', headers=None, data=None,
                     callback=None, errors=STRICT, **params):
        params.update({'apikey': self.api_key})
        request = getattr(requests, method.lower())
        r = request(service_url, headers=headers, data=data, params=params)
        return r.json()

    def get_location(self, code='BKK'):
        loc_key = "loc-{code}".format(code=code)
        path = "location/{code}".format(code=code)
        service_url = "{url}/{path}".format(url=self.api_url, path=path)
        loc_data = self.make_request(service_url)

        return loc_data

    def search_airport(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path='search-airport')
        return self.make_request(service_url, **params)

    def search_circle(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path='search-circle')
        return self.make_request(service_url, **params)

    def extensive_search(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path='extensive-search')
        return self.make_request(service_url, **params)


class Flights(Transport):

    def __init__(self, api_key, api_url=API_URL):
        self.api_url = "{api_url}/flights".format(api_url=api_url)
        self.api_key = api_key

    def inspiration_search(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path='inspiration-search')
        return self.make_request(service_url, **params)

    def auto_complete(self, **params):
        api_url = "{api_url}/airports".format(api_url=API_URL)
        service_url = "{url}/{path}".format(
            url=api_url, path='autocomplete')
        return self.make_request(service_url, **params)

    def low_fare_search(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path='low-fare-search')
        return self.make_request(service_url, **params)


class Hotels(Transport):

    def __init__(self, api_key, api_url=API_URL):
        super(Hotels, self).__init__(api_key=api_key, api_url=api_url)
        self.api_url = "{api_url}/hotels".format(api_url=api_url)

    def search_property_code(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path=params['property_code'])
        return self.make_request(service_url, **params)


class Cars(Transport):

    def __init__(self, api_key, api_url=API_URL):
        super(Cars, self).__init__(api_key=api_key, api_url=api_url)
        self.api_url = "{api_url}/cars".format(api_url=api_url)


class CO2Emissions(Transport):

    def __init__(self, api_key, api_url=API_URL):
        super(CO2Emissions, self).__init__(api_key=api_key, api_url=api_url)
        self.api_url = "{api_url}/CO2".format(api_url=api_url)

    def get_data(self, **params):
        return self.make_request(self.api_url, **params)


class RailStations(Transport):

    def __init__(self, api_key, api_url=API_URL):
        super(RailStations, self).__init__(api_key=api_key, api_url=api_url)
        self.api_url = "{api_url}/rail-stations".format(api_url=api_url)

    def auto_complete(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path='autocomplete')
        return self.make_request(service_url, **params)

    def nearest_relevant(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path='nearest-relevant')
        return self.make_request(service_url, **params)

    def get_info(self, **params):
        # special case where the API path is different
        api_url = "{api_url}/rail-station".format(api_url=API_URL)
        service_url = "{url}/{path}".format(
            url=api_url, path=params['id'])
        return self.make_request(service_url, **params)


class Trains(Transport):

    def __init__(self, api_key, api_url=API_URL):
        super(Trains, self).__init__(api_key=api_key, api_url=api_url)
        self.api_url = "{api_url}/trains".format(api_url=api_url)

    def schedule_search(self, **params):
        service_url = "{url}/{path}".format(
            url=self.api_url, path='schedule-search')
        return self.make_request(service_url, **params)
