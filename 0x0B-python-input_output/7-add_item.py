#!/usr/bin/python3
"""adds item"""


import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(fil_ename):
    obj = load_from_json_file(file_name)
else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, file_name)
