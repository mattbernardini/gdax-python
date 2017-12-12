#!/bin/python
# import PyMongo and connect to a local, running Mongo instance
from pymongo import MongoClient
import gdax
mongo_client = MongoClient("mongodb://localhost:27017/")
from websocket import WebSocketConnectionClosedException
# specify the database and collection
db = mongo_client.cryptocurrency_database
BTC_collection = db.BTC_collection
ETH_collection = db.ETH_collection
LTC_collection = db.LTC_collection
# instantiate a WebsocketClient instance, with a Mongo collection as a parameter
wsClientBTC_USD = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="BTC-USD",
  mongo_collection=BTC_collection, should_print=False)
wsClientETH_USD = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="ETH-USD",
  mongo_collection=ETH_collection, should_print=False)
wsClientLTC_USD = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="LTC-USD",
  mongo_collection=LTC_collection, should_print=False)
while (True):
      try:
        wsClientBTC_USD.start()
        wsClientETH_USD.start()
        wsClientLTC_USD.start()
      except WebSocketConnectionClosedException as e:
        print("\nCaught an exception")
        if wsClientBTC_USD.stop:
          print("\nwsClientBTC_USD broke")
          wsClientBTC_USD.close()
          wsClientBTC_USD.start()
        elif wsClientETH_USD.stop:
          print("\nwsClientETH_USD broke")
          wsClientETH_USD.close()
          wsClientETH_USD.start()
        elif wsClientLTC_USD.stop:
          print("\nwsClientLTC_USD broke")
          wsClientLTC_USD.close()
          wsClientLTC_USD.start()
        
