from pymongo import MongoClient
import json

if __name__ == '__main__':
    client = MongoClient('10.200.12.66', 27017, maxPoolSize=50)
    db = client.THE_AKOM_TEST_LAB_Official
    mycol = db["_AKOM_types_acbtype_refactor"]

    mylist = json.load(open('d:/_work/_program/_python/mongo_new_types.json', 'r'))
    x = mycol.insert_many(mylist)
    #print mylist
