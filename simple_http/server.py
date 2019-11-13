import json
import traceback
from flask import Flask


class Server(Flask):
    r"""
    Example code, which runs a server with two APIs: "test_fn_1" and
    "test_fn_2".

    ```
    app = Server('test')

    @app.add('test_fn_1')
    def test_fn_1(x):
        return [x + 1]

    @app.add('test_fn_2')
    def test_fn_2(x):
        raise ValueError('Hold on brother. This is just a test.')

    app.run('localhost', 8000)
    ```
    """

    def __init__(self, name, **kwargs):
        self._app_name = name
        super().__init__(name, **kwargs)

        self._max_id = 0

    def add(self, name):
        """Returns a decorator."""

        def wrapper(fn):
            rule = '/app/{}/{}/<kwargs_json>'.format(self._app_name, name)

            def jsonfied_fn(kwargs_json):
                kwargs = json.loads(kwargs_json)
                try:
                    result = fn(**kwargs)
                    result_dict = {
                        'result': json.dumps(result),
                        'error': '',
                    }
                except Exception:
                    error_msg = traceback.format_exc()
                    result_dict = {
                        'result': '',
                        'error': error_msg,
                    }
                result_json = json.dumps(result_dict)
                return result_json

            unique_id = self._max_id
            self._max_id += 1
            jsonfied_fn.__name__ = str(unique_id)  # TODO
            return self.route(rule)(jsonfied_fn)

        return wrapper
