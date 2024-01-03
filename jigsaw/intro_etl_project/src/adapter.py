from coin import Coin

class CoinAdapter:
    #create a dictionary for each coin record, to use as input for our coin objects
    def select_attributes(self, coin_record):
        id = coin_record['id']
        symbol = coin_record['symbol']
        name = coin_record['name']
        current_price = coin_record['current_price']
        market_cap = coin_record['market_cap']
        market_cap_rank = coin_record['market_cap_rank']
        coin_record_dict = {'id':id, 'symbol':symbol, 'name':name, 'current_price':current_price, 'market_cap':market_cap, 'market_cap_rank':market_cap_rank}
        return coin_record_dict
    
    #create coin object for each dictionary
    def create_coin(self, coin_records):
        coins = []
        for coin_record in coin_records:
            coin_attrs = self.select_attributes(coin_record)
            coin = Coin(**coin_attrs)
            coins.append(coin)
        return coins
    


