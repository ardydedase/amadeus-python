===============================
Amadeus Python Library
===============================

.. image:: https://img.shields.io/travis/ardydedase/amadeus-python.svg
        :target: https://travis-ci.org/ardydedase/amadeus-python

.. image:: https://img.shields.io/pypi/v/amadeus.svg
        :target: https://pypi.python.org/pypi/amadeus

.. image:: https://readthedocs.org/projects/amadeus/badge/?version=latest
        :target: https://readthedocs.org/projects/amadeus/?badge=latest
        :alt: Documentation Status

Python Package for Amadeus Travel Innovation Sandbox

* Free software: BSD license
* Amadeus Travel Innovation Sandbox Documentation: https://sandbox.amadeus.com/apis
* Python Package Documentation: https://amadeus.readthedocs.org.

Disclaimer
----------

Amadeus is a trademark registered by Amadeus IT Group. The Python Library is created and maintained by Ardy Dedase and is not associated with nor endorsed by Amadeus. Therefore Amadeus has no responsibilities or liabilities in relation to the use of this code.

Background
----------

After participating in a startup event sponsored by Amadeus, I realized that the code I started will be helpful to those who will use Amadeus' Sandbox API in the future. So I decided to make it available as a Python package and share it on Github.

Features
--------

* :airplane:: **Flight Inspiration Search** allows you to answer the question: *Where can I go within a given travel budget?*
* :airplane:: **Extensive Flight Search** allows you to answer the question: *When is the best date to fly?*
* :airplane:: **Low-Fare Search** lets you find the cheapest one way or return itineraries.
* :hotel:: **Hotel Lowest Price Search** by center point/radius and by latitude/longitude window.
* :car:: **Car Rental Availability Search** by center point/radius and by airport.
* :train:: **Trains & Rail** supports Rail station auto-complete and information.
* :factory:: **CO2 Emissions Data** average per passenger by origin and destination.
* :white_check_mark:: Tested on Python 2.6, 2.7, 3.3 and 3.4 for this release.

Installation
------------

At the command line::

    $ pip install amadeus

Or::

    $ easy_install amadeus

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv amadeus
    $ pip install amadeus

Usage
-----

Before anything else, make sure that you have created an account and have gotten your API key from Amadeus: https://sandbox.amadeus.com/ 

Read the docs: http://amadeus.readthedocs.org/en/latest/usage.html    

Or


Read the code: `amadeus/amadeus.py` and `tests/test_amadeus.py`
