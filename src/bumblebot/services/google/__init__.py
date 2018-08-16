from random import randint

import requests
from requests import HTTPError


class GoogleClient:
    api_key: str
    custom_search_id: str = '000622945010313952938:hl4t8y1jy3o'
    uri: str = 'https://www.googleapis.com/customsearch/v1'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def find_image(self, q: str, animated: bool = False):
        data = {
            'q': q,
            'cx': self.custom_search_id,
            'searchType': 'image',
            'fields': 'items/link',
            'key': self.api_key
        }
        if animated:
            data['hq'] = 'gif'

        data['start'] = randint(1, 5)

        try:
            result = requests.get(self.uri, params=data)
            result.raise_for_status()
            result = result.json()
            return result['items'][randint(0, len(result['items']) - 1)]['link']
        except ValueError:
            return None
        except HTTPError:
            return None
