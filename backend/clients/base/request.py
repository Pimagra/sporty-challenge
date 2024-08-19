import json
from dataclasses import dataclass

import requests


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


default_headers = {"Content-Type": "application/json", "Accept": "application/json"}


def get_headers(additional):
    headers = default_headers
    if additional is not None:
        headers.update(additional)

    return headers


class APIRequest:
    def get(self, url, headers=None, params=None):
        headers = get_headers(headers)
        response = requests.get(url, headers=headers, params=params)
        return self.get_response(response)

    def post(self, url, payload, headers=None):
        headers = get_headers(headers)
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return self.get_response(response)

    def delete(self, url, headers=None):
        headers = get_headers(headers)
        response = requests.delete(url, headers)
        return self.get_response(response)

    def get_response(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(status_code, text, as_dict, headers)
