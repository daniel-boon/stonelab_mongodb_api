from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from pymongo import MongoClient 
import json
from bson.json_util import dumps
from bson.json_util import loads
from connection.settings import Database_connection

#database class
database = Database_connection()
client = database.client
mydb = client['stonelab']
collection = mydb['customers']

app = FastAPI()

# def check_connection(database):
#     '''check_connection('database_name') 
    
#     to check connection'''
#     try:
#         client.server_info()
#         print('SUCESSFULLY CONNECTED TO -> {}'.format(database))
#     except:
#         print('CONNECTION ERROR!')


# http://127.0.0.1:8000/v1/mahistory/?start_date='2020-01-17'&end_date='2020-01-18'
@app.get('/v1/mahistory/')
async def ma_history(start_date: str, end_date: str):
    # database.check_connection()
    print('start date', start_date)
    print('end date', end_date)
    myquery = { "address": "Park Lane 38" }

    mydoc = collection.find(myquery)


    list_cur = list(mydoc)
    result = dumps(list_cur,sort_keys=True,ensure_ascii=True)
    result = json.loads(result.replace("\'", '"'))

    return result

#uvicorn main:app --reload