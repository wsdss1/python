import json
import uuid
import copy

sum = 0
file_rez = 'd:/_work/_program/_python/mongo_new.json'
file_def = 'd:/_work/_program/_python/mongo.json'

def rezdic(one):
    rez = []
    global sum
    sum += len(one['chargeHalls'])
    for item in one['chargeHalls']:
        res_item = copy.deepcopy(one)
        del res_item['chargeHalls']
        del res_item['_id']
        res_item['chargeHallId'] = item['chargeHallId']
        res_item['programName'] = item['programName']
        rez.append(res_item)
    return rez

if __name__ == '__main__':
    rez_all = []
    with open(file_def) as json_data:
        d = json.load(json_data)
        for item in d:
            rez_all.extend(rezdic(item))

        for i, x in enumerate(rez_all):
            x['programId'] = f'{i + 1}'
            # x['_id']['$oid'] = uuid.uuid4().hex[:24] нет надобности использовать, т.к. данный id генерит сама MongoDB

        print(sum)
        file = open(file_rez, 'w')
        file.write(json.dumps(rez_all))
        file.close()