========
Usage
========

To use Amadeus Python Library in a project::

    import amadeus

Flights
~~~~~~~

https://sandbox.amadeus.com/apis#flights

Flight Inspiration Search API::

        from amadeus import Flights

        flights = Flights('<Your API Key>')
        resp = flights.inspiration_search(
            origin='BKK',
            departure_date="2015-11-25--2015-11-30",
            max_price=200)

Extensive Flight Search API::

        from amadeus import Flights

        flights = Flights('<Your API Key>')
        resp = flights.extensive_search(
            origin='NCE',
            destination='LAS',
            departure_date='2015-11-25--2015-11-30',
            duration='4--10')

Low Fare Search API::

        from amadeus import Flights

        flights = Flights('<Your API Key>')
        resp = flights.low_fare_search(
            origin='NCE',
            destination='LAS',
            departure_date='2015-11-25',
            return_date='2015-11-30',
            duration='4--10')

Airport Autocomplete::

        from amadeus import Flights

        flights = Flights('<Your API Key>')
        resp = flights.auto_complete(term='Ban')        
        print(resp)          


Hotel Lowest Price Search
~~~~~~~~~~~~~~~~~~~~~~~~~

https://sandbox.amadeus.com/apis#hotels

Search center point and radius::

        from amadeus import Hotels

        hotels = Hotels('<Your API Key>')
        resp = hotels.search_circle(
            check_in='2015-11-25',
            check_out='2015-11-30',
            latitude=16.44671,
            longitude=102.833,
            currency='USD',
            max_rate=100,
            radius=300)

Search by latitude/longitude window::

        from amadeus import Hotels

        hotels = Hotels('<Your API Key>')
        resp = hotels.search_airport(
            check_in='2015-11-25',
            check_out='2015-11-30',
            location='BKK',
            currency='USD',
            max_rate=100)

Car Rental Availability Search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://sandbox.amadeus.com/content/cars

Search by airport::

        from amadeus import Cars

        cars = Cars('<Your API Key>')
        resp = cars.search_airport(
            pick_up='2015-11-25',
            drop_off='2015-11-30',
            location='BKK',
            currency='USD',
            lang='EN')

Search center point and radius::

        from amadeus import Cars

        cars = Cars('<Your API Key>')
        resp = cars.search_circle(
            pick_up='2015-11-25',
            drop_off='2015-11-30',
            latitude=16.44671,
            longitude=102.833,
            radius=70,
            currency='USD',
            lang='EN')


Rail and Train
~~~~~~~~~~~~~~

Rail Station Auto Complete::

        from amadeus import RailStations
        rails = RailStations('<Your API Key>')
        resp = rails.auto_complete(term='VENT')


Rail Station Get info::

        from amadeus import RailStations
        rails = RailStations('<Your API Key>')
        resp = rails.get_info(id=8301700)

CO2 Emissions
~~~~~~~~~~~~~

https://sandbox.amadeus.com/content/CO2

Get emissions data::

        from amadeus import CO2Emissions

        co2 = CO2Emissions('<Your API Key>')
        resp = co2.get_data(
            origin='PAR',
            destination='NYC')