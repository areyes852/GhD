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
currency_pair='BTC-EUR'
prezoSpot=client.get_spot_price(currency_pair=currency_pair)
prezoCompra=client.get_buy_price(currency_pair= currency_pair)
prezoVenta=client.get_sell_price(currency_pair=currency_pair)

tempo=time.time()
actualizarPrecios(prezoCompra, prezoVenta, prezoSpot,tempo)
print 'Prezo compra: ' + str(obterPrezoCompra(tempo))
print 'Prezo venta: ' + str(obterPrezoVenta(tempo))
print 'Prezo Spot: ' + str(obterPrezoSpot(tempo))
