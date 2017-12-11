#!/bin/python
# import PyMongo and connect to a local, running Mongo instance
from pymongo import MongoClient
import gdax
mongo_client = MongoClient("mongodb://localhost:27017/")

# specify the database and collection
db = mongo_client.cryptocurrency_database
BTC_collection = db.BTC_collection
ETH_collection = db.ETH_collection
LTC_collection = db.LTC_collection
# instantiate a WebsocketClient instance, with a Mongo collection as a parameter
wsClient1 = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="BTC-USD",
  mongo_collection=BTC_collection, should_print=False)
wsClient2 = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="ETH-USD",
  mongo_collection=ETH_collection, should_print=False)
wsClient3 = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="LTC-USD",
  mongo_collection=LTC_collection, should_print=False)
wsClient1.start()
wsClient2.start()
wsClient3.start()
