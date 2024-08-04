import json
import threading
import time
import random


def read_json(file_name):
    with open(file_name,'r') as json_file:
        data = json.load(json_file)
        info = json.dumps(data)
        print(f'the information in file {file_name} is {info}')
    time.sleep((random.randint(1,4)))



json_files = ['file.json','file2.json']

thread_list = []
for json_file in json_files:
    t = threading.Thread(target=read_json, args=(json_file,))
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()