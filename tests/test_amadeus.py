#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_amadeus
----------------------------------

Tests for `amadeus` module.
"""

import unittest

from datetime import datetime, timedelta

from amadeus.amadeus import (
    Transport, Flights, Hotels, Cars, CO2Emissions, RailStations, Trains)

try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

API_URL = 'https://api.sandbox.amadeus.com/v1.2'
# Update the API KEY
API_KEY = 'xx5nE3UgOfRAwCFw9pw2WAwKiWojqMRR'

# mock if API Key is not available
if not API_KEY:
    mock_return_value = ['flights', 'hotels', 'cars']
    Transport.make_request = Mock(return_value=mock_return_value)


class AmadeusTestCase(unittest.TestCase):

    def setUp(self):
        self.api_key = API_KEY

        datetime_format = '%Y-%m'
        outbound_datetime = datetime.now() + timedelta(days=7)
        inbound_datetime = outbound_datetime + timedelta(days=31)
        self.outbound = outbound_datetime.strftime(datetime_format)
        self.inbound = inbound_datetime.strftime(datetime_format)

        datetime_format = '%Y-%m-%d'
        inbound_datetime = outbound_datetime + timedelta(days=3)
        self.departure_date = outbound_datetime.strftime(datetime_format)
        self.return_date = inbound_datetime.strftime(datetime_format)

        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass


class TestTransport(AmadeusTestCase):

    def test_get_location(self):
        transport = Transport(self.api_key)
        resp = transport.get_location('BKK')
        self.assertTrue(len(resp) > 0)


class TestFlights(AmadeusTestCase):

    def setUp(self):
        super(TestFlights, self).setUp()

    def test_inspiration_search(self):
        flights = Flights(self.api_key)

        origin = 'BKK'
        departure_date = self.departure_date
        return_date = self.return_date
        max_price = 200

        resp = flights.inspiration_search(
            origin=origin,
            departure_date="{departure_date}--{return_date}".format(
                departure_date=departure_date, return_date=return_date),
            max_price=max_price)

        self.assertTrue(len(resp) > 0)

    def test_extensive_search(self):
        flights = Flights(self.api_key)

        origin = 'NCE'
        destination = 'LAS'
        departure_date = self.departure_date
        return_date = self.return_date
        duration = '4--10'

        resp = flights.extensive_search(
            origin=origin,
            destination=destination,
            departure_date="{departure_date}--{return_date}".format(
                departure_date=departure_date, return_date=return_date),
            duration=duration)

        print(resp)

        self.assertTrue(len(resp) > 0)

    def test_low_fare_search(self):
        flights = Flights(self.api_key)

        origin = 'NCE'
        destination = 'LAS'
        duration = '4--10'

        resp = flights.low_fare_search(
            origin=origin,
            destination=destination,
            departure_date=self.departure_date,
            return_date=self.return_date,
            duration=duration)

        self.assertTrue(len(resp) > 0)

    def test_auto_complete(self):
        flights = Flights(self.api_key)
        resp = flights.auto_complete(term='Ban')
        self.assertTrue(len(resp) > 0)


class TestHotels(AmadeusTestCase):

    def setUp(self):
        super(TestHotels, self).setUp()
        datetime_format = '%Y-%m-%d'
        checkin_datetime = datetime.now()
        checkout_datetime = checkin_datetime + timedelta(days=4)
        self.check_in = checkin_datetime.strftime(datetime_format)
        self.check_out = checkout_datetime.strftime(datetime_format)

    def test_search_circle(self):
        hotels = Hotels(self.api_key)

        latitude = 16.44671
        longitude = 102.833
        currency = 'USD'
        max_rate = 100

        resp = hotels.search_circle(
            check_in=self.check_in,
            check_out=self.check_out,
            latitude=latitude,
            longitude=longitude,
            currency=currency,
            max_rate=max_rate,
            radius=300)

        self.assertTrue(len(resp) > 0)

    def test_search_airport(self):
        hotels = Hotels(self.api_key)

        location = 'BKK'
        currency = 'USD'
        max_rate = 100

        resp = hotels.search_airport(
            check_in=self.check_in,
            check_out=self.check_out,
            location=location,
            currency=currency,
            max_rate=max_rate)

        self.assertTrue(len(resp) > 0)

    def test_search_property_code(self):
        hotels = Hotels(self.api_key)

        property_code = 'RTNCEPUL'
        currency = 'USD'
        max_rate = 100

        resp = hotels.search_property_code(
            check_in=self.check_in,
            check_out=self.check_out,
            property_code=property_code,
            currency=currency,
            max_rate=max_rate)

        self.assertTrue(len(resp) > 0)


class TestCars(AmadeusTestCase):

    def setUp(self):
        super(TestCars, self).setUp()
        datetime_format = '%Y-%m-%dT%H:%S'
        pickup_datetime = datetime.now() + timedelta(days=10)
        dropoff_datetime = pickup_datetime + timedelta(days=3)
        self.pick_up = pickup_datetime.strftime(datetime_format)
        self.drop_off = dropoff_datetime.strftime(datetime_format)

    def test_search_airport(self):
        cars = Cars(self.api_key)

        currency = 'USD'
        max_rate = 100
        latitude = 16.44671
        longitude = 102.833
        location = 'BKK'

        resp = cars.search_airport(
            pick_up=self.pick_up,
            drop_off=self.drop_off,
            location=location,
            currency=currency,
            lang='EN')

        self.assertTrue(len(resp) > 0)

    def test_search_circle(self):
        cars = Cars(self.api_key)

        currency = 'USD'
        max_rate = 100
        latitude = 16.44671
        longitude = 102.833
        location = 'BKK'

        resp = cars.search_circle(
            pick_up=self.pick_up,
            drop_off=self.drop_off,
            latitude=latitude,
            longitude=longitude,
            radius=70,
            currency=currency,
            lang='EN')

        self.assertTrue(len(resp) > 0)


class TestCO2Emissions(AmadeusTestCase):

    def test_get_data(self):
        co2 = CO2Emissions(self.api_key)
        resp = co2.get_data(
            origin='PAR',
            destination='NYC')

        self.assertTrue(len(resp) > 0)


class TestRailStations(AmadeusTestCase):

    def test_auto_complete(self):
        rails = RailStations(self.api_key)
        resp = rails.auto_complete(term='VENT')
        self.assertTrue(len(resp) > 0)

    def test_nearest_relevant(self):
        rails = RailStations(self.api_key)
        resp = rails.nearest_relevant(latitude=41.89021, longitude=12.492231)
        self.assertTrue(len(resp) > 0)

    def test_get_info(self):
        rails = RailStations(self.api_key)
        resp = rails.get_info(id=8301700)
        self.assertTrue(len(resp) > 0)


class TestTrains(AmadeusTestCase):

    def test_extensive_search(self):
        trains = Trains(self.api_key)
        resp = trains.extensive_search(
            origin=8399003,
            destination=8308409,
            departure_date=self.departure_date)
        self.assertTrue(len(resp) > 0)

    def test_schedule_search(self):
        trains = Trains(self.api_key)
        resp = trains.schedule_search(
            origin=8302589,
            departure_date=self.departure_date)

        self.assertTrue(len(resp) > 0)

if __name__ == '__main__':
    unittest.main()
