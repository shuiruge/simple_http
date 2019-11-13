import json
from urllib.parse import quote
from urllib.request import urlopen


class Client(object):
    """
    Example code
    ```
    # First set up an HTTP server

    app = Server('test')

    @app.add('test_fn_1')
    def test_fn_1(x):
        return [x + 1]

    @app.add('test_fn_2')
    def test_fn_2(x):
        raise ValueError('Hold on brother. This is just a test.')

    app.run('localhost', 8000)

    # Then visiting the HTTP server by a client

    client = Client('test', 'localhost', 8000)
    client.get('test_fn_1', x=1)  # => [2]
    client.get('test_fn_2', x=1)  # raise an error.
    ```
    """

    def __init__(self, app_name, hostname, port):
        self._app_name = app_name
        self._server_address = '{0}:{1}'.format(hostname, port)

    def get(self, method_name, **kwargs):
        """Returns an object the API returns, or raises an error if
        the API returns an error."""
        kwargs_json = json.dumps(kwargs)
        url = self._get_url(method_name, kwargs_json)
        response_json = self._get_responce(url)
        result_dict = json.loads(response_json)
        if result_dict['result']:
            return json.loads(result_dict['result'])
        else:
            raise Exception(result_dict['error'])

    def _get_url(self, method_name, kwargs_json):
        # Since URL cannot accept "/", replace by whitespace
        kwargs_json = kwargs_json.replace('/', '-')
        url = 'http://{0}/app/{1}/{2}/{3}'.format(
            self._server_address, self._app_name, method_name,
            quote(kwargs_json))
        return url

    def _get_responce(self, url):
        return urlopen(url).read()
