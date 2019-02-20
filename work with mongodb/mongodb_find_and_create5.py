import json
import copy

file_with_old_and_new_id = 'd:/_work/_program/_python/prName_hallId_prId_format.json'
file_types_acbtype_refactor = 'd:/_work/_program/_python/_AKOM_types_acbtype_refactor.json'
file_rezult = 'd:/_work/_program/_python/_AKOM_types_acbtype_refactor_with_true_id.json'

def rezdic(doc1_element, doc2):
    result_element = []
    doc1_element_copy = copy.deepcopy(doc1_element)
    del doc1_element_copy['_id']
    for charge_hall in doc1_element_copy['chargeHalls']:
        for index, program_id in enumerate(charge_hall['programId']):
            for element in doc2:
                if charge_hall['hallId'] == element['chargeHallId'] and  element['programId'] == program_id:
                    charge_hall['programId'][index] = element['new_prid']
                    break

    result_element.append(doc1_element_copy)
    return result_element


if __name__ == '__main__':
    result_all_elements = []
    with open(file_types_acbtype_refactor) as json_data:
        doc1 = json.load(json_data)
    with open(file_with_old_and_new_id) as json_data:
        doc2 = json.load(json_data)
        for doc1_element in doc1:
            result_all_elements.extend(rezdic(doc1_element, doc2))

    print(result_all_elements)
    file = open(file_rezult, 'w')
    file.write(json.dumps(result_all_elements))
    file.close()