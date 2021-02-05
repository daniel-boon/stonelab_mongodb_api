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
import datetime
# print ('Current date/time: {}'.format(datetime.datetime.now()))

app = FastAPI()

#database class
database = Database_connection()
client = database.client
mydb = client['stonelab']
# ma_collection = mydb['history_ma']
# repair_collection = mydb['history_repair']
stonelabdata= mydb['history_new_data']

#API calling example
# http://127.0.0.1:8000/v1/mahistory/?plant_id=1&start_date='2020-01-17'&end_date='2020-01-18'
# plan 2 http://127.0.0.1:8000/v1/stonelab/?plant_alias=FL&start_date=2020-04-21&end_date=2020-04-22

@app.get('/v1/stonelab/')
async def ma_repair_data(plant_alias: str, start_date: str, end_date: str):
    # database.check_connection()

    #use variables from query parameters
    # print('plant id', plant_id)
    print('plant alias', plant_alias)
    print('start date', start_date)
    print('end date', end_date)

    print(str(plant_alias))
    print(str(start_date))
    print(str(end_date))

    # myquery1 = {"plant_alias": plant_alias}
    
    myquery = {"plantAlias": plant_alias, "actualdate": dict() }

    if start_date is not None:
        myquery["actualdate"]["$gte"] = start_date

    if end_date is not None:
        myquery["actualdate"]["$lte"] = end_date

    
 
    print(myquery)
    mydoc = stonelabdata.find(myquery)

    list_cur = list(mydoc)
    result = dumps(list_cur,sort_keys=True,ensure_ascii=True)
    result = json.loads(result.replace("\'", '"'))

    def get_data(self, name):
        for data in self.__data:
            if data['actualdate'] == startdatetime:
                return student

    return JSONResponse(status_code=200, content=result)
    


#uvicorn main:app --reload