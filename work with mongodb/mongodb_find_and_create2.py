import json
import copy

file_rez = 'd:/_work/_program/_python/prName_hallId_prId_old.json'
file_def = 'd:/_work/_program/_python/_AKOM_programs_acbprog_old.json'

def rezdic(one):
    rez = []
    for item in one['chargeHalls']:
        rez_d = {}
        #res_item = copy.deepcopy(one)
        rez_d['programName'] = item['programName']
        rez_d['chargeHallId'] = item['chargeHallId']
        rez_d['programId'] = one['programId']
        rez.append(rez_d)
    return rez

if __name__ == '__main__':
    rez_all = []
    with open(file_def) as json_data:
        d = json.load(json_data)
        for item in d:
            rez_all.extend(rezdic(item))

        print(rez_all)

        file = open(file_rez, 'w')
        file.write(json.dumps(rez_all))
        file.close()