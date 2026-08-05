import requests

class DexscreenerAPI:
    BASE_URL = "https://api.dexscreener.com"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_coin_data(self, coin_id):
        url = f"{self.BASE_URL}/v1/coins/{coin_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_rugged_coins(self):
        url = f"{self.BASE_URL}/v1/coins/rugged"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_pumped_coins(self):
        url = f"{self.BASE_URL}/v1/coins/pumped"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_tier1_coins(self):
        url = f"{self.BASE_URL}/v1/coins/tier1"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_cex_listed_coins(self):
        url = f"{self.BASE_URL}/v1/coins/cex-listed"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()