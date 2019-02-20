from pymongo import MongoClient
from bson.json_util import dumps

if __name__ == '__main__':
    client = MongoClient('10.200.12.66', 27017, maxPoolSize=50)
    db = client.THE_AKOM_TEST_LAB_Official
    collection = db['_AKOM_types_acbtype_old']
    print(collection.count())
    cursor = collection.find()

    file = open('d:/_work/_program/_python/_AKOM_types_acbtype_old.json', 'w')
    file.write(dumps(cursor))
    file.close()