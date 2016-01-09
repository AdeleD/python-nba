from requests.exceptions import ConnectionError

try:
    import urllib.parse as urlrequest
except ImportError:
    import urllib as urlrequest

import requests


class NBAStatsAPI():
    def __init__(self):
        self.api_url = 'http://stats.nba.com/stats/'

    def request(self, endpoint, params):
        params = params or {}
        encoded_params = urlrequest.urlencode(params)

        url = self.format_url(endpoint, encoded_params)

        try:
            result = requests.get(url)
        except ConnectionError as e:
            raise Exception('Unable to connect to stats.nba.com. %s' % e)

        if result.content:
            return result.json()

    def format_url(self, endpoint, encoded_params):
        return '%s%s?%s' % (self.api_url, endpoint, encoded_params)
