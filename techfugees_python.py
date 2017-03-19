'''
Documentation, License etc.

@package techfugees_python
'''
import json
import pprint
json_data=open("test.json").read()

data = json.loads(json_data)
print(data["maps"])
