"""
A Python library for consuming the Rate Beer JSON API
"""

import requests

class RateBeer(object):
    """
    Provides an abstraction to consume the Rate Beer API.
    """

    QUERY_URL = 'http://ratebeer.com/json/bff.asp'

    def __init__(self, api_key):
        """
        :api_key: Your RateBeer API key
        :raises ValueError: If api_key is empty
        """
        if not api_key:
            raise ValueError('Cannot query RateBeer without an API  key')
        self.k = api_key

    def get_beer(self, beerid):
        """
        Fetch a beer by unique beerid.

        :beerid: the unique ratebeer id of the beer to fetch
        :returns:
        :raises HTTPException: If an http response other than 200 is
                               returned when querying ratebeer
        """
        
        r = requests.get(self.QUERY_URL, params={'bd': beerid, 'k': self.k})
        
        if r.status_code != requests.codes.ok:
            r.raise_for_status()
        
        result = r.json()
        if len(result) == 1:
            return result[0]
        else:
            return None

    def find_beer(self, name):
        """
        Search for a beer by name

        :name:
        :returns:
        :raises:
        """

        r = requests.get(self.QUERY_URL, params={'bn': name, 'k': self.k})

        if r.status_code != requests.codes.ok:
            r.raise_for_status()
        
        return r.json()