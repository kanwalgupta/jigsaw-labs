from client import Client
from coin import Coin
from adapter import CoinAdapter

client = Client()
coin_records = client.make_request()
coins = CoinAdapter().create_coins(coin_records)

print(Coin.rank_by_price_change_percentage(coins))
#print([coin.__dict__ for coin in coins])


