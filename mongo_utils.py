import os
import json
from datetime import datetime

MONGO_URI = os.getenv("MONGO_URI")
USE_TEST_MODE = not MONGO_URI
RESULTS_FILE = "results.json"

if USE_TEST_MODE:
    print("⚠️  TEST MODE: Using local JSON file instead of MongoDB")
    collection = None
else:
    from pymongo import MongoClient
    client = MongoClient(MONGO_URI)
    db = client["crypto_recovery"]
    collection = db["results"]

def save_to_mongo(address, private, balance):
    doc = {"address": address, "private": private, "balance": balance, "timestamp": datetime.now().isoformat()}
    
    if USE_TEST_MODE:
        try:
            with open(RESULTS_FILE, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        
        existing = next((i for i, item in enumerate(data) if item['address'] == address), None)
        if existing is not None:
            data[existing] = doc
        else:
            data.append(doc)
        
        with open(RESULTS_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"💾 Saved to {RESULTS_FILE}: {address}")
    elif collection is not None:
        collection.update_one({"address": address}, {"$set": doc}, upsert=True)
