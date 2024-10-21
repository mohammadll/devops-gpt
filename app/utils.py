
import os
from fastapi import HTTPException
from pymongo import MongoClient
def get_mongo_client():

    client = MongoClient(host=os.environ.get('MONGO_HOST'),
                            port=int(os.environ.get('MONGO_PORT')),
                            username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'), 
                            password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'))
    
    return client



def get_mongo_collection():

    client = get_mongo_client()
    col = client[os.environ.get('MONGO_INITDB_DATABASE')]['qa']
    return col
        
        
def save_QA_to_mongo(question:str, answer:str) -> None:

    try:

        col = get_mongo_collection()

        data = {

            "question":question,
            "answer":answer
        }

        col.insert_one(data)

    except Exception as e:

        raise HTTPException(status_code=400,detail=str(e))