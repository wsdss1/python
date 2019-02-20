import json
import uuid
import copy

file_def = 'd:/_work/_program/_python/mongo_types.json'
file_rez = 'd:/_work/_program/_python/mongo_new_types.json'

def rezdic(one):
    rez = []
    a = {   "hallId":"_hall1",
            "maxBlockCapacity" : 18,
            "minBlockCapacity" : 0,
            "maxTableCapacity" : 180,
            "minTableCapacity" : 18
        }

    b = {   "hallId": "_hall2",
            "maxBlockCapacity": 22,
            "minBlockCapacity": 0,
            "maxTableCapacity": 176,
            "minTableCapacity": 22
        }

    res_item = copy.deepcopy(one)
    del res_item['defaultProgramId']
    del res_item['programId']
    del res_item['_id']
    res_item['typeGroup'] = None
    rez_a = copy.deepcopy(a)
    rez_a['programId'] = one['programId']
    rez_b = copy.deepcopy(b)
    rez_b['programId'] = one['programId']
    res_item['chargeHalls'] = [rez_a, rez_b]

    rez.append(res_item)
    return rez

if __name__ == '__main__':
    rez_all = []
    with open(file_def) as json_data:
        d = json.load(json_data)
        for item in d:
            rez_all.extend(rezdic(item))

        file = open(file_rez, 'w')
        file.write(json.dumps(rez_all))
        file.close()