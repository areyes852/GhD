# -*- coding: utf-8 -*-

import sys
import os
import time
import sqlite3
from BDBtc import *
from coinbase.wallet.client import Client
crearBDBtc()
[apiKey,apiSecret]=obterCredenciales()
client = Client(apiKey,apiSecret)
currencyPair='ETH-EUR'

while 1:
    prezoSpot=client.get_spot_price(currency=currencyPair)
    prezoCompra=client.get_buy_price(currency_pair=currencyPair)
    prezoVenta=client.get_sell_price(currency_pair=currencyPair)

    tempo=time.time()

    actualizarPrecios(prezoCompra['amount'], prezoVenta['amount'], prezoSpot['amount'],tempo)
    time.sleep(10)
    print ('Prezo compra: ' + str(obterPrezoCompra(tempo)))
    # print 'Prezo venta: ' + str(obterPrezoVenta(tempo))
    # print 'Prezo Spot: ' + str(obterPrezoSpot(tempo))


# print prezoSpot['amount']
# print prezoCompra['amount']
# print prezoVenta['amount']
#
#
# print 'Prezo compra: ' + str(obterPrezoCompra(tempo))
# print 'Prezo venta: ' + str(obterPrezoVenta(tempo))
# print 'Prezo Spot: ' + str(obterPrezoSpot(tempo))
