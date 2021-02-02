from glob import glob, iglob
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import json
import pprint

load_dotenv('connection/.env')

MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PWD = os.environ.get("MONGODB_PWD")
MONGODB_PORT = os.environ.get("MONGODB_PORT")

client = MongoClient('mongodb://{}:{}@{}:{}'.format(MONGODB_USER,MONGODB_PWD,MONGODB_HOST,MONGODB_PORT))
mydb = client['stonelab']
mycol_ma = mydb['history_ma']
mycol_repair =mydb['history_repair']

mycol_newData = mydb['history_new_data']

path = './finalData'
files = os.listdir(path)
# print(files)


# ----------------------------------------------------------------------------------------------
for i in files:
    finalFile = open('finalData/{}'.format(i))
    print(finalFile)
    finalData = json.load(finalFile)
    finalDataRusult = mycol_newData.insert_many(finalData)
    finalFile.close()
    # print("1")


# ----------------------------------------------------------------------------------------------

# mafile1 = open('jsonFiles/ma_plant21_2020-01-01_to_2020-01-31.json')
# mafile2 = open('jsonFiles/ma_plant21_2020-02-01_to_2020-02-29.json')
# mafile4 = open('jsonFiles/ma_plant21_2020-04-01_to_2020-04-30.json')
# mafile5 = open('jsonFiles/ma_plant21_2020-05-01_to_2020-05-31.json')
# mafile6 = open('jsonFiles/ma_plant21_2020-06-01_to_2020-06-30.json')
# mafile7 = open('jsonFiles/ma_plant21_2020-07-01_to_2020-07-31.json')
# mafile8 = open('jsonFiles/ma_plant21_2020-08-01_to_2020-08-31.json')
# mafile9 = open('jsonFiles/ma_plant21_2020-09-01_to_2020-09-30.json')
# mafile10 = open('jsonFiles/ma_plant21_2020-10-01_to_2020-10-31.json')
# mafile11 = open('jsonFiles/ma_plant21_2020-11-01_to_2020-11-30.json')

# madata1 = json.load(mafile1)
# maresult = mycol_ma.insert_many(madata1)
# mafile1.close()
# print("1")

# madata2 = json.load(mafile2)
# maresult = mycol_ma.insert_many(madata2)
# mafile2.close()
# print("2")

# madata4 = json.load(mafile4)
# maresult = mycol_ma.insert_many(madata4)
# mafile4.close()
# print("4")

# madata5 = json.load(mafile5)
# maresult = mycol_ma.insert_many(madata5)
# mafile5.close()
# print("5")

# madata6 = json.load(mafile6)
# maresult = mycol_ma.insert_many(madata6)
# mafile6.close()
# print("6")

# madata7 = json.load(mafile7)
# maresult = mycol_ma.insert_many(madata7)
# mafile7.close()
# print("7")

# madata8 = json.load(mafile8)
# maresult = mycol_ma.insert_many(madata8)
# mafile8.close()
# print("8")

# madata9 = json.load(mafile9)
# maresult = mycol_ma.insert_many(madata9)
# mafile9.close()
# print("9")

# madata10 = json.load(mafile10)
# maresult = mycol_ma.insert_many(madata10)
# mafile10.close()
# print("10")

# madata11 = json.load(mafile11)
# maresult = mycol_ma.insert_many(madata11)
# mafile11.close()
# print("11")

# ----------------------------------------------------------------------------------------------

# repairfile1 = open('jsonFiles/repair_plant21_2020-01-01_to_2020-01-31.json')
# repairfile2 = open('jsonFiles/repair_plant21_2020-02-01_to_2020-02-29.json')
# repairfile4 = open('jsonFiles/repair_plant21_2020-04-01_to_2020-04-30.json')
# repairfile5 = open('jsonFiles/repair_plant21_2020-05-01_to_2020-05-31.json')
# repairfile6 = open('jsonFiles/repair_plant21_2020-06-01_to_2020-06-30.json')
# repairfile7 = open('jsonFiles/repair_plant21_2020-07-01_to_2020-07-31.json')
# repairfile8 = open('jsonFiles/repair_plant21_2020-08-01_to_2020-08-31.json')
# repairfile9 = open('jsonFiles/repair_plant21_2020-09-01_to_2020-09-30.json')
# repairfile10 = open('jsonFiles/repair_plant21_2020-10-01_to_2020-10-31.json')
# repairfile11 = open('jsonFiles/repair_plant21_2020-11-01_to_2020-11-30.json')

# repairdata1 = json.load(repairfile1)
# repairresult = mycol_repair.insert_many(repairdata1)
# repairfile1.close()
# print("1")

# repairdata2 = json.load(repairfile2)
# repairresult = mycol_repair.insert_many(repairdata2)
# repairfile2.close()
# print("2")

# repairdata4 = json.load(repairfile4)
# repairresult = mycol_repair.insert_many(repairdata4)
# repairfile4.close()
# print("4")

# repairdata5 = json.load(repairfile5)
# repairresult = mycol_repair.insert_many(repairdata5)
# repairfile5.close()
# print("5")

# repairdata6 = json.load(repairfile6)
# repairresult = mycol_repair.insert_many(repairdata6)
# repairfile6.close()
# print("6")

# repairdata7 = json.load(repairfile7)
# repairresult = mycol_repair.insert_many(repairdata7)
# repairfile7.close()
# print("7")

# repairdata8 = json.load(repairfile8)
# repairresult = mycol_repair.insert_many(repairdata8)
# repairfile8.close()
# print("8")

# repairdata9 = json.load(repairfile9)
# repairresult = mycol_repair.insert_many(repairdata9)
# repairfile9.close()
# print("9")

# repairdata10 = json.load(repairfile10)
# repairresult = mycol_repair.insert_many(repairdata10)
# repairfile10.close()
# print("10")

# repairdata11 = json.load(repairfile11)
# repairresult = mycol_repair.insert_many(repairdata11)
# repairfile11.close()
# print("11")

# ----------------------------------------------------------------------------------------------

# Test
# jsonFilePath = os.getcwd() + '/jsonFiles'
# allFiles = os.listdir(jsonFilePath)
# for fileName in allFiles:
#     if fileName.startswith('ma_plant'):
#         print(fileName)

# ----------------------------------------------------------------------------------------------


# repairfile = open('jsonFiles/repair_plant21_2020-02-01_to_2020-02-29.json')
# repairdata = json.load(repairfile)
# repairresult = mycol_repair.insert_many(repairdata)
# repairfile.close()


# madatafile = ('ma_plant{}_{}-{}-{}_to_{}-{}-{}.json'.format(plantId,sYear,sMonth,sDay,eYear,eMonth,eDay))

# directory = os.fsencode("/Users/panusronphansod/Documents/github/stonelab_mongodb_api/jsonFiles")

# malists = (glob('*/ma_plant*.json'))
# repairlists = (glob('*/repair_plant*.json'))
# print(malists)
# print(repairlists)

# malistsjsons = ['jsonFiles/ma_plant14_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant11_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant4_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant12_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant4_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant11_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant21_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant14_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant2_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant15_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant15_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant10_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant5_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant5_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant10_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant15_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant8_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant15_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant3_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant13_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant21_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant6_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant6_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant21_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant5_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant13_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant3_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant8_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant21_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant9_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant2_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant12_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant21_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant12_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant7_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant7_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant21_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant12_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant2_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant2_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant9_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant21_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant21_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant14_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant4_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant4_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant11_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant11_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant4_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant14_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant14_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant3_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant15_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant5_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant10_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant10_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant13_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant5_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant15_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant3_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant3_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant8_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant6_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant21_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant13_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant13_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant21_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant13_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant6_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant8_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant3_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant2_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant9_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant21_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant7_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant21_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant12_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant4_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant12_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant21_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant7_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant21_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant9_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant2_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant14_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant5_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant10_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant15_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant8_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant10_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant10_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant5_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant21_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant4_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant7_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant11_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant21_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant14_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant14_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant21_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant11_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant4_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant7_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant7_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant12_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant21_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant9_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant2_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant21_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant21_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant21_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant2_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant9_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant21_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant12_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant7_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant6_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant13_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant21_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant8_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant8_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant3_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant3_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant8_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant21_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant13_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant21_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant6_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant10_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant10_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant5_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant15_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant15_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant5_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant10_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant6_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant11_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant11_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant4_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant21_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant14_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant14_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant9_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant4_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant11_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant21_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant12_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant21_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant11_2020-02-01_to_2020-02-29.json', 'jsonFiles/ma_plant7_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant21_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant2_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant9_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant9_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant9_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant2_2020-07-01_to_2020-07-31.json', 'jsonFiles/ma_plant21_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant7_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant12_2020-10-01_to_2020-10-31.json', 'jsonFiles/ma_plant21_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant21_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant13_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant6_2020-09-01_to_2020-09-30.json', 'jsonFiles/ma_plant21_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant3_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant8_2020-11-01_to_2020-11-30.json', 'jsonFiles/ma_plant8_2020-06-01_to_2020-06-30.json', 'jsonFiles/ma_plant3_2020-05-01_to_2020-05-31.json', 'jsonFiles/ma_plant6_2020-04-01_to_2020-04-30.json', 'jsonFiles/ma_plant6_2020-01-01_to_2020-01-31.json', 'jsonFiles/ma_plant13_2020-08-01_to_2020-08-31.json', 'jsonFiles/ma_plant21_2020-11-01_to_2020-11-30.json']
# for malistsjson in malistsjsons:
#     with open(malistsjson) as m:
#         ma_data = json.load(m)  # load data from JSON to dict
#         for k, v in ma_data.items(): 
#             mycol_ma.insert_one(v) 

# for ma_data in iglob(os.path.expanduser('jsonFiles/ma_plant*.json')):
#         with open(ma_data) as madata:
#             mafiles = json.load(madata)
#             print("done ma")
#             for mafile in mafiles:
#                 mycol_ma.insert_one(mafile)
#                 print("done ma2")
# madata.close()

# for repair_data in iglob(os.path.expanduser('jsonFiles/repair_plant*.json')):
#         with open(repair_data) as repairdata:
#             repairfiles = json.load(repairdata)
#             print("done repair")
#             for repairfile in repairfiles:
#                 mycol_repair.insert_one(repairfile)
#                 print("done repair2")
# repairdata.close()


# ma = open(glob('jsonFiles/ma_plant*.json'))
# repair = open(glob('jsonFiles/repair_plant*.json'))
# data_ma = json.load(ma)
# data_repair = json.load(repair)

# # print(data)
# result_ma = mycol_ma.insert_many(data_ma)
# result_repair = mycol_repair.insert_many(data_repair)
# ma.close()
# repair.close()