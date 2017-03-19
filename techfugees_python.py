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
    best_mentor = dict()
    best_mentor_score = 999
    for mentor in mentor_data:
#        print(mentor)
        help_score = Levenshtein.distance(mentee["Help Need"],mentor["Help Offered"]);
         #       print("Goal Match: ",100-Levenshtein.distance(mentee["Goal"],mentor["Goal"]))
        #print("Help Match:\t",100-help_score)
        #print("Language Match:\t",100-Levenshtein.distance(mentee["Language"],mentor["Language"]),)
#        print("Strengths Match: ",100-Levenshtein.distance(mentee["Strengths"],mentor["Strengths"]),)
#        print("Interests Match: ",100-Levenshtein.distance(mentee["Interests"],mentor["Interests"]),)
        if help_score < best_mentor_score:
            best_mentor = mentor
            best_mentor_score = help_score
    print (best_mentor)
    print("Help Match:\t",100-best_mentor_score,"\n")

        
