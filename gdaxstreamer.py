#!/bin/python
# import PyMongo and connect to a local, running Mongo instance
from pymongo import MongoClient
import gdax
mongo_client = MongoClient("mongodb://localhost:27017/")
from websocket import WebSocketConnectionClosedException
# specify the database and collection
db = mongo_client.cryptocurrency_database
collection = db.unifiedCollection
# instantiate a WebsocketClient instance, with a Mongo collection as a parameter
unifiedWsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products=["BTC-USD","ETH-USD","LTC-USD",]
  mongo_collection=collection, should_print=False)
unifiedWsClient.start()
        
