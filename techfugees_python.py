'''
Documentation, License etc.

@package techfugees_python
'''
import json
import pprint
import Levenshtein

mentor_json=open("mentor.json").read()
mentee_json=open("mentee.json").read()

mentor_data = json.loads(mentor_json)
mentee_data = json.loads(mentee_json)

pprint.pprint(mentor_data[0])
pprint.pprint(mentee_data)

for mentee in mentee_data:
    print(mentee)
    print(mentee["Goal"])
    for mentor in mentor_data:
        print(mentor)
        print(Levenshtein.distance(mentee["Goal"],mentor["Goal"]))
        print(Levenshtein.distance(mentee["Language"],mentor["Language"]))
        
