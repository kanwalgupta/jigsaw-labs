class Coin:
    def __init__(self, id, symbol, name, current_price, market_cap, market_cap_rank, price_change_percentage_30d_in_currency):
        self.id = id 
        self.symbol = symbol
        self.name = name
        self.current_price = current_price
        self.market_cap = market_cap
        self.market_cap_rank = market_cap_rank
        self.price_change_percentage_30d_in_currency = price_change_percentage_30d_in_currency

    def rank_by_price_change_percentage(coins:list) -> list:
        coin_dicts = [coin.__dict__ for coin in coins]
        #check for null values before sorting
        for coin_dict in coin_dicts:
            if coin_dict['price_change_percentage_30d_in_currency'] is None:
                coin_dict['price_change_percentage_30d_in_currency'] = 0
        sorted_coin_dicts = sorted(coin_dicts, key=lambda x: x['price_change_percentage_30d_in_currency'], reverse=True)
        top_ten = sorted_coin_dicts[:10]
        return top_ten
       

