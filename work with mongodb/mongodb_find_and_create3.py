import json
import copy

file_rez = 'd:/_work/_program/_python/prName_hallId_prId_new.json'
file_def = 'd:/_work/_program/_python/_AKOM_programs_acbprog_refactor_new_id.json'

def rezdic(one):
    rez = []
    rez_d = {}
    res_item = copy.deepcopy(one)
    rez_d['programName'] = item['programName']
    rez_d['chargeHallId'] = item['chargeHallId']
    rez_d['programId'] = res_item['programId']
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