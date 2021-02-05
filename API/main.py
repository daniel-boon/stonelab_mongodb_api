from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from pymongo import MongoClient 
import json
from bson.json_util import dumps
from bson.json_util import loads

load_dotenv('.env')

MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PWD = os.environ.get("MONGODB_PWD")
MONGODB_PORT = os.environ.get("MONGODB_PORT")

client = MongoClient('mongodb://{}:{}@{}:{}'.format(MONGODB_USER,MONGODB_PWD,MONGODB_HOST,MONGODB_PORT))
mydb = client['stonelab']
mycol = mydb['history_ma'],['history_repair']

app = FastAPI()

def check_connection(database):
    '''check_connection('database_name') 
    
    to check connection'''
    try:
        client.server_info()
        print('SUCESSFULLY CONNECTED TO -> {}'.format(database))
    except:
        print('CONNECTION ERROR!')

@app.get('/v1/mahistory/')
async def ma_history():
    myquery = { "address": { "$gt": "S" } }
    mydoc = mycol.find(myquery)

    list_cur = list(mydoc)
    result = dumps(list_cur,sort_keys=True,ensure_ascii=True)
    result = json.loads(result.replace("\'", '"'))

    return result

