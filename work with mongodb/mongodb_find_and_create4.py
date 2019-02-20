import json
import copy

file_rez = 'd:/_work/_program/_python/prName_hallId_prId_new.json'
file_def = 'd:/_work/_program/_python/prName_hallId_prId.json'
file_rez1 = 'd:/_work/_program/_python/prName_hallId_prId_format.json'

print("\u04140\u0417\u0410\u0420\u042f\u04145"== "75 EFB")

if __name__ == '__main__':
    rez_all = []
    with open(file_def) as json_data:
        d1 = json.load(json_data)
        res_item1 = copy.deepcopy(d1)
    with open(file_rez) as json_data:
        d2 = json.load(json_data)
        res_item2 = copy.deepcopy(d2)
        for item in res_item1:
            finded = False
            for next in res_item2:
                if item['programName'] == next['programName'] and item['chargeHallId'] == next['chargeHallId']:
                    print(f"{item['programName'], next['programName'],item['chargeHallId'], next['chargeHallId']}")
                    item['new_prid'] = next['programId']
                    finded =True
                    break
            if not finded:
                print("!!!!!!!!")

    print(res_item1)
    file = open(file_rez1, 'w')
    file.write(json.dumps(res_item1))
    file.close()