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

liftOfName = ["CP Food Lab (Head Office) ใช้งานส่วนของ Calibration",
              "CPF Egg Processing - Nong Jok",
              "CPF Feed Bangna",
              "CPF Feed Hadyai",
              "CPF Feed Khon Kaen",
              "CPF Feed Korat (โคกกรวด)",
              "CPF Feed Lamphun",
              "CPF Feed Nongkhae (BPF)",
              "CPF Feed Pak Thong Chai",
              "CPF Feed Rajburi",
              "CPF Feed Sriracha",
              "CPF Feed Tharnkasem Saraburi",
              "CPF Feed Tharua",
              "CPF Feed พิษณุโลก",
              "CPF Food Processing Minburi 2",
              "เจริญโภคภัณฑ์อาหาร จำกัด (มหาชน)",
              "บริษัท ซีพีเอฟ (ประเทศไทย) จำกัด (มหาชน) (CPF ธุรกิจไก่กระทงมีนบุรี)",
              "บริษัท ซีพีเอฟ (ประเทศไทย) จำกัด (มหาชน) (CPF ธุรกิจไก่กระทงโคราช)",
              "บริษัท ซีพีเอฟ (ประเทศไทย) จำกัด (ไก่ปู่ย่าพันธุ์ ฟาร์มบัวชุม ลพบุรี สาขาที่ 00204)",
              "บริษัท ซีพีเอฟ (ประเทศไทย)จำกัด(มหาชน) (CPF ธุรกิจไก่กระทงสระบุรี)",
              "บริษัท ซีพีเอฟ ฟู้ด โชคชัย (ประเทศไทย) จำกัด (มหาชน)]"]


def get_plant_alias(id):
    if id == 0:
        return None
    return listOfId[id-1]

def get_plant_name(id):
    if id == 0:
        return None
    return liftOfName[id-1]

# for id in range(1, 22):
#     print(str(id) + ": " + get_plant_alias(id))


path = "./jsonFiles"

files = os.listdir(path)

total_file = len(files)

for i in range(total_file):
    file = files[i]

    # print(file)
    result = re.match("^repair_plant(\d+)_", file)
    if result:
        # print(result)
        id = int(result.group(1))
        name = get_plant_alias(id)
        fullname = get_plant_name(id)
        print("{}\t {}\t: {}".format(fullname, name, file))

        ma_file = open("{}/{}".format(path, file))
        madata = json.load(ma_file)

        for data in madata:
            data["plantAlias"] = name
            data["plantName"] = fullname

        with open("./edited/edited_" + file, 'w', encoding='utf-8') as fp:
            json.dump(madata, fp, ensure_ascii=False)

        print("{} %".format(float((i + 1) * 100.0 / total_file)))
