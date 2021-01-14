import os
from os.path import join, dirname
from dotenv import load_dotenv
from pymongo import MongoClient 

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PWD = os.environ.get("MONGODB_PWD")
MONGODB_PORT = os.environ.get("MONGODB_PORT")

class Database_connection:
    '''To connect the database 
       Database_connection('database_name','collection_name')
       
       To check the connection use method
       
       check_connection()
    '''
    def __init__(self,database,collection):
        self.client = MongoClient('mongodb://{}:{}@{}:{}'.format(MONGODB_USER,MONGODB_PWD,MONGODB_HOST,MONGODB_PORT))
        self.database = database
        self.collection = collection
    
    def check_connection(self):
        '''Check database connection

        Success output: SUCESSFULLY CONNECTED TO -> database_name 

        Fail output: CONNECTION ERROR!'''

        client = self.client
        database = self.database
        try:
            client.server_info()
            print('SUCESSFULLY CONNECTED TO -> {}'.format(database))
        except:
            print('CONNECTION ERROR!')

    