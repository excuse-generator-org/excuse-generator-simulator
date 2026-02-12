from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["excuse_db"]

excuse_collection = db["excuses"]
users_collection = db["users"]
