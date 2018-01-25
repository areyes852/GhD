# -*- coding: utf-8 -*-

import sys
import os
import time
import sqlite3
import requests
from BDBtc import *
from coinbase.wallet.client import Client


crearBDBtc()
#
# [apiKey,apiSecret]=['Vioq9ZeOIyvt98Zw','68yCkxPl5EAHXhIMGDDCdHXIfwXrXWrO']
# API_VERSION = '2016-02-18'
# client = Client(apiKey,apiSecret,API_VERSION)
# currencyPair='ETH-EUR'


while 1:
    rBuy = requests.get("https://api.coinbase.com/v2/prices/ETH-EUR/buy").json()
    rSell = requests.get("https://api.coinbase.com/v2/prices/ETH-EUR/sell").json()
    rSpot = requests.get("https://api.coinbase.com/v2/prices/ETH-EUR/spot").json()
    prezoCompra = rBuy['data']['amount']
    prezoVenta = rSell['data']['amount']
    prezoSpot = rSpot['data']['amount']

    tempo=time.time()

    actualizarPrecios(prezoCompra, prezoVenta, prezoSpot,tempo)
    print 'Prezo compra: ' + str(obterPrezoCompra(tempo))
    print 'Prezo venta: ' + str(obterPrezoVenta(tempo))
    print 'Prezo Spot: ' + str(obterPrezoSpot(tempo))
    time.sleep(5)
