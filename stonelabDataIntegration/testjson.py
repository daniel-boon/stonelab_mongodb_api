import json
import os
from collections import defaultdict

mafileaccess = open('jsonFiles/ma_plant2_2020-01-01_to_2020-01-31.json')
madata = json.load(mafileaccess)

for i in madata:
    print(i['toolRemark'])
    
