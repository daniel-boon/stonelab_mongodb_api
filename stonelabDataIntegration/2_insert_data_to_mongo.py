import os
from dotenv import load_dotenv
from pymongo import MongoClient 
import json

load_dotenv('.env')

MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PWD = os.environ.get("MONGODB_PWD")
MONGODB_PORT = os.environ.get("MONGODB_PORT")

client = MongoClient('mongodb://{}:{}@{}:{}'.format(MONGODB_USER,MONGODB_PWD,MONGODB_HOST,MONGODB_PORT))
mydb = client['stonelab']
mycol = mydb['customers']

f = open('jsonFiles/ma_plant2_2020-06-01_to_2020-06-30.json') 
data = json.load(f)
# print(data)
result = mycol.insert_many(data)
f.close() 