'''
Documentation, License etc.

@package techfugees_python
'''
import json
import pprint
import Levenshtein

mentor_json=open("mentor_data.json").read()
mentee_json=open("mentee_data.json").read()

mentor_data = json.loads(mentor_json)
mentee_data = json.loads(mentee_json)

#pprint.pprint(mentor_data[0])
#pprint.pprint(mentee_data)

for mentee in mentee_data:
    print(mentee)
#    print(mentee["Goal"])
    for mentor in mentor_data:
        print(mentor)
 #       print("Goal Match: ",100-Levenshtein.distance(mentee["Goal"],mentor["Goal"]))
        print("Help Match:\t",100-Levenshtein.distance(mentee["Help Need"],mentor["Help Offered"]))
        print("Language Match:\t",100-Levenshtein.distance(mentee["Language"],mentor["Language"]),)
#        print("Strengths Match: ",100-Levenshtein.distance(mentee["Strengths"],mentor["Strengths"]),)
#        print("Interests Match: ",100-Levenshtein.distance(mentee["Interests"],mentor["Interests"]),)
        
