import os
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)
PATH = './edited'

PATH_TO_SAVE = './mapped'

files = os.listdir(PATH)
total_file = len(files)

for i in range(total_file):
    file = files[i]
    path_to_file = os.path.join(PATH, file)

    new_file_name = file.replace("edited_", "")
    new_path = os.path.join(PATH_TO_SAVE, new_file_name)

    with open(path_to_file, 'r') as f2:
        data = f2.read()

        json_data = json.loads(data)
        
        result = []
        for obj in json_data:
            # Clone obj to be obj_copy
            obj_copy = obj.copy()
            
            # delete key 'checkSheetItems'
            del obj['checksheetItems']
            
            for x in obj_copy['checksheetItems']:
                # no key named 'checksheetItems'
                temp = obj.copy()

                for key in x.keys():
                    new_key = 'checksheetItem' + key.capitalize()
                    
                    temp[new_key] = x[key]

                # append temp into result
                result.append(temp)

        with open(new_path, 'w', encoding='utf-8') as fp:
            json.dump(result, fp, ensure_ascii=False)

        print("{} %".format(float((i + 1) * 100.0 / total_file)))

