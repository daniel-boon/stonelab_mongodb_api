from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from pymongo import MongoClient 
import json
from bson.json_util import dumps
from bson.json_util import loads
from connection.settings import Database_connection

app = FastAPI()

#database class
database = Database_connection()
client = database.client
mydb = client['stonelab']
collection = mydb['customers']



#API calling example
# http://127.0.0.1:8000/v1/mahistory/?plant_id=1&start_date='2020-01-17'&end_date='2020-01-18'
@app.get('/v1/mahistory/')
async def ma_history(plant_id: int, start_date: str, end_date: str):
    # database.check_connection()

    #use variables from query parameters
    print('plant id', plant_id)
    print('start date', start_date)
    print('end date', end_date)

    myquery = { "address": "Park Lane 38" }
    mydoc = collection.find(myquery)

    list_cur = list(mydoc)
    result = dumps(list_cur,sort_keys=True,ensure_ascii=True)
    result = json.loads(result.replace("\'", '"'))

    return JSONResponse(status_code=200, content=result)


#uvicorn main:app --reload