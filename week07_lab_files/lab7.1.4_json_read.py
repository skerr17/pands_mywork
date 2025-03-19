# this program reads a json file 
# and prints the contents of the file
# Author: Stephen Kerr

import json

FILENAME = "testdict.json"

def readDict():
    with open(FILENAME) as f:
        return json.load(f)

some_dict = readDict()   
print(some_dict)