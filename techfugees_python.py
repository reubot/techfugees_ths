'''
Documentation, License etc.

@package techfugees_python
'''
import json
import pprint
mentor_json=open("mentor.json").read()
mentee_json=open("mentee.json").read()

mentor_data = json.loads(mentor_json)
mentee_data = json.loads(mentee_json)

pprint.pprint(mentor_data)
pprint.pprint(mentee_data)
