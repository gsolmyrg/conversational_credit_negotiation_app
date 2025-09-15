import os

import requests


class CreditNegotiationService:
    def __init__(self):
        self.middleware_url = os.getenv("MIDDLEWARE_URL")
        self.middleware_path = os.getenv("MIDDLEWARE_PATH")
        self.middleware_api_key = os.getenv("MIDDLEWARE_API_KEY")

    def negotiate_credit(self, data: dict):
        self._notify_middleware(data)

    def _notify_middleware(self, data: dict):
        url = f"{self.middleware_url}/{self.middleware_path}"
        headers = {"Authorization": f"Bearer {self.middleware_api_key}"}
        requests.post(url, headers=headers, json=data)
