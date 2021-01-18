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
    def __init__(self):
        self.mongodb_host = MONGODB_HOST
        self.mongodb_user = MONGODB_USER
        self.mongodb_pwd = MONGODB_PWD
        self.mongodb_port = MONGODB_PORT
        self.client = MongoClient('mongodb://{}:{}@{}:{}'.format(MONGODB_USER,MONGODB_PWD,MONGODB_HOST,MONGODB_PORT))
    
    def check_connection(self):
        '''Check database connection

        Success output: SUCESSFULLY CONNECTED - return True
        
        Fail output: CONNECTION ERROR! - return False
        
        '''

        client = self.client

        try:
            client.server_info()
            print('SUCESSFULLY CONNECTED')
            return True
        except:
            print('CONNECTION ERROR!')
            return False

    