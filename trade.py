import requests, json
from config import *
from datetime import datetime
from threading import Timer
import numpy, websocket, threading, talib

DATA_URL = 'https://data.alpaca.markets/v1'
LASTTRADE_URL = '/v1/last/stocks/'

SOCKET = 'wss://data.alpaca.markets/stream
'

BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
today = datetime.today()
y = today.replace(day=today.day+1, hour=9, minute=30, second=0, microsecond=0)
delta_t = y-today
secs = delta_t.seconds+1


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)


def get_last_trade(symbol):
    r = requests.get(DATA_URL + LASTTRADE_URL + '{}'.format(symbol), headers=HEADERS)
    print(r)
    return 0


#response = create_order('AAPL', 100, 'buy', 'market', 'gtc')

#orders = get_orders()
#print(response)
#print(orders)

last_trade = get_last_trade('SPY')
print(last_trade)