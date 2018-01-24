import gdax                          #https://github.com/danpaquin/gdax-python
from pymongo import MongoClient

public_client = gdax.PublicClient()
mongo_client = MongoClient('mongodb://localhost:27017/')

precio=public_client.get_product_ticker(product_id='ETH-EUR')
print(precio['price'])

# Paramaters are optional
wsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com",
                                products=["BTC-EUR", "ETH-EUR"])

                                # specify the database and collection
db = mongo_client.cryptocurrency_database
BTC_collection = db.BTC_collection


# Do other stuff...
wsClient.close()
