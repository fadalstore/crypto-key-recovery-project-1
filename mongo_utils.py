import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
db = client["crypto_recovery"]
collection = db["results"]

def save_to_mongo(address, private, balance):
    doc = {"address": address, "private": private, "balance": balance}
    collection.update_one({"address": address}, {"$set": doc}, upsert=True)
