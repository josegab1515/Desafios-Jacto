import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_mongo_connection():
    client = MongoClient(os.getenv("MONGO_URI"))
    return client[os.getenv("MONGO_DB")]