import json
import copy

file_rez = 'd:/_work/_program/_python/programId_hallId.json'
file_def = 'd:/_work/_program/_python/_AKOM_types_acbtype_refactor.json'

def rezdic(one):
    rez = []
    for item in one['chargeHalls']:
        res_item = copy.deepcopy(item)
        del res_item['maxBlockCapacity']
        del res_item['minBlockCapacity']
        del res_item['maxTableCapacity']
        del res_item['minTableCapacity']
        rez.append(res_item)
    return rez

if __name__ == '__main__':
    rez_all = []
    n = []
    with open(file_def) as json_data:
        d = json.load(json_data)
        for item in d:
            rez_all.extend(rezdic(item))
        for i in rez_all:
            if i not in n:
                n.append(i)
        print(n)
        print(rez_all)

        file = open(file_rez, 'w')
        file.write(json.dumps(n))
        file.close()