import unittest
from unittest.mock import patch

from requests import Response

from bumblebot.services.google import GoogleClient


class TestGoogle(unittest.TestCase):
    @patch(target='requests.get')
    def test_find_image(self, requests_get):
        google = GoogleClient('fake_api_key')
        # fail HTTP
        r = Response()
        r.status_code = 500
        requests_get.return_value = r
        result = google.find_image('fake_string')
        self.assertIsNone(result)
        # fail value
        r = Response()
        r.status_code = 200
        r._content = b'fake_bad_json'
        requests_get.return_value = r
        result = google.find_image('fake_string')
        self.assertIsNone(result)
        # success not animated
        r = Response()
        r.status_code = 200
        r._content = b'{"items": [{"link": "fake_result"}]}'
        requests_get.return_value = r
        result = google.find_image('fake_string')
        args, kwargs = requests_get.call_args
        self.assertIn('params', kwargs)
        self.assertNotIn('hq', kwargs['params'])
        self.assertEqual(result, 'fake_result')
        # success animated
        r = Response()
        r.status_code = 200
        r._content = b'{"items": [{"link": "fake_result"}]}'
        requests_get.return_value = r
        result = google.find_image('fake_string', True)
        args, kwargs = requests_get.call_args
        self.assertIn('params', kwargs)
        self.assertIn('hq', kwargs['params'])
        self.assertEqual(kwargs['params']['hq'], 'gif')
        self.assertEqual(result, 'fake_result')
