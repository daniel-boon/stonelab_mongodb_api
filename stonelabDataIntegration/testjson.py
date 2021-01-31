import json
import os
import re
import pprint
from collections import defaultdict

# mafileaccess = open('jsonFiles/ma_plant2_2020-01-01_to_2020-01-31.json')
# madata = json.load(mafileaccess)

# for i in madata:
#     print(i['submitBy'])

pp = pprint.PrettyPrinter(indent=2)

listOfId = ["FL", "NJ", "BKF", "HYF", "KKF", "KRF", "LPF", "BPF", "PTF", "RBF",
            "SRF", "TKF", "TRF", "PLF", "MB2", "IT", "MB1", "KR", "LB", "SB", "CC", ]

def get_plant_alias(id):
    if id == 0:
        return None
    return listOfId[id-1]

# for id in range(1, 22):
#     print(str(id) + ": " + get_plant_alias(id))

path = "./jsonFiles"

files = os.listdir(path)

total_file = len(files)

for i in range(total_file):
    file = files[i]

    # print(file)
    result = re.match("^ma_plant(\d+)_", file)
    if result:
        # print(result)
        id = int(result.group(1))
        name = get_plant_alias(id)
        # print("{0}\t: {1}".format(name, file))

        ma_file = open("{0}/{1}".format(path, file))
        madata = json.load(ma_file)
        
        for data in madata:
            data["plantAlias"] = name

        with open( "./edited/edited_" + file, 'w', encoding='utf-8') as fp:
            json.dump(madata, fp, ensure_ascii=False)

        print("{0} %".format(float((i + 1) * 100.0 / total_file)))
        