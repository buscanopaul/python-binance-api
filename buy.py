from binance.client import Client
from binance.enums import *
import time

client = Client('binance-api-key', 'binance-secret-key')
print('logged in')

# info = client.get_account()

# bal = info['balances']
# for b in bal:
#     if float(b['free']) > 0:
#         print(b['asset'])

balance = client.get_asset_balance(asset='BTC')
portion_balance = float(balance['free'])

name = input('Enter coin: ')

coin = name.upper() + 'BTC'

buy_market = client.order_market_buy(
    symbol= coin,
    quoteOrderQty= portion_balance)

print(coin)

print(balance)

print(portion_balance)

print(buy_market)
