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
print ('Current date/time: {}'.format(datetime.datetime.now()))

app = FastAPI()

#database class
database = Database_connection()
client = database.client
mydb = client['stonelab']
collection = mydb['history_ma']

#API calling example
# http://127.0.0.1:8000/v1/mahistory/?plant_id=1&start_date='2020-01-17'&end_date='2020-01-18'
# plan 2 http://127.0.0.1:8000/v1/mahistory/?start_date=2020-04-21&end_date=2020-04-22

@app.get('/v1/mahistory/')
async def ma_history(start_date: str, end_date: str):
    # database.check_connection()

    #use variables from query parameters
    # print('plant id', plant_id)
    print('start date', start_date)
    print('end date', end_date)

    # start_date = str("2020-04-21 10:58:18")
    # objstart = datetime.datetime.strptime(strstart, "%Y-%m-%d %H:%M:%S.%f")

    # end_date = str("2020-04-22 02:52:25")
    # objend = datetime.datetime.strptime(strend, "%Y-%m-%d %H:%M:%S.%f")
    
    # print('Date:', date_time_obj.date())
    # print('Time:', date_time_obj.time())
    print('Date-time Start:', start_date)
    print('Date-time End:', end_date)
    print(str(start_date))
    print(str(end_date))
    
    myquery = { "actualdate": dict() }

    if start_date is not None:
        myquery["actualdate"]["$gte"] = start_date

    if end_date is not None:
        myquery["actualdate"]["$lte"] = end_date

    # {"^gte": objstart }, "^lte": objend
    print(myquery)
    mydoc = collection.find(myquery).limit(100)

    list_cur = list(mydoc)
    result = dumps(list_cur,sort_keys=True,ensure_ascii=True)
    result = json.loads(result.replace("\'", '"'))

    return JSONResponse(status_code=200, content=result)


#uvicorn main:app --reload