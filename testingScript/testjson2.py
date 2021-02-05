import json
import os

# delete address
# with open('test.json', 'r') as data_file:
#     data = json.load(data_file)
# for element in data:
#     element.pop('address', None)
# with open('test_after.json', 'w') as data_file:
#     data = json.dump(data, data_file)

# loop small array
with open('testFolder/test.json', 'r') as data_file:
    data = json.load(data_file)

data_len = len(data)
for x in range(0,data_len):
    address_len = len(data[x]['address'])
    print("length =",address_len)
    for y in range(0,address_len):
        sub_address = data[x]['address'][y] 
        print("result =",sub_address)

with open('test_after.json', 'w') as data_file:
    data = json.dump(data, data_file)