from client import Client
from coin import Coin
from adapter import CoinAdapter

client = Client()
coin_records = client.make_request()
coins = CoinAdapter().create_coin(coin_records)

print([coin.__dict__ for coin in coins])
