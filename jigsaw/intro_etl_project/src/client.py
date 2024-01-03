import requests

class Client:
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&locale=en'

    def make_request(self):
        response = requests.get(self.url)
        coin_records = response.json()
        return coin_records