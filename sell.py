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

name = input('Enter coin: ')

balance = client.get_asset_balance(asset=name.upper())
portion_balance = float(balance['free'])

coin = name.upper() + 'BTC'

sell_market = client.order_market_sell(
    symbol= coin,
    quoteOrderQty= portion_balance)

print(coin)

print(balance)

print(portion_balance)

print(sell_market)
