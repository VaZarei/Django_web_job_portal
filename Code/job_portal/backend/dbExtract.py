import os
import django
import json

# Set the Django project path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal.settings')
django.setup()

# Now you can import models
from job_application.models import JobApplication


obj = JobApplication.objects.get(id=1)
print(type(obj.__dict__))
dictobj = obj.__dict__

# print(dictobj.keys())
# print(dictobj.values())

# for key in dictobj.keys():
#     print(key), print(dictobj[key])
#     print("*"*20)

newdict = {}
experienceLevel = {}
jobTypes = {}
positions = []
locations = []
checkboxes= {}
languages = {}
personalInfo = {}
eeo = {}

"""
for key in dictobj.keys():
    splitted_word = key.split('_')
    if len(splitted_word)<2 :
        
        newdict[splitted_word[0]] = dictobj[key]
"""    


blockwords = ["_state", "user_id" ]
for key in dictobj.keys():
    #print("key:", key, "___    value: ", dictobj[key])

    if blockwords[0] == key.lower() or blockwords[1] == key.lower():
        continue
        
    splitted_word = key.split('_')
    

    if len(splitted_word)==1 :
        newdict[splitted_word[0]] = dictobj[key]

    
    elif splitted_word[0] == "experienceLevel" :
        experienceLevel[splitted_word[1]] = dictobj[key]

    elif splitted_word[0] == "jobTypes" :
        jobTypes[splitted_word[1]] = dictobj[key]

    elif splitted_word[1] == "position" :         ###### position in models change to positions pls
        positions.append(dictobj[key] )

    elif splitted_word[1] == "location" :         ###### location in models change to locations pls
        locations.append(dictobj[key] )

    elif splitted_word[0] == "checkboxes" :
        checkboxes[splitted_word[1]] = dictobj[key]

    elif splitted_word[0] == "language" :
        languages[dictobj[key]] = "'Native or bilingual'"   ### language to languages and delete the null

    elif splitted_word[0] == "personalInfo" :

        if "First".lower() in splitted_word[1].lower() :
            splitted_word[1] = "First Name"

        if "Last".lower() in splitted_word[1].lower() :
            splitted_word[1] = "Last Name"
        
        if "Country".lower() in splitted_word[1].lower() :
            splitted_word[1] = "Phone Country Code"
        
        if "Mobile".lower() in splitted_word[1].lower() :
            splitted_word[1] = "Mobile Phone Number"
        
        if "Street".lower() in splitted_word[1].lower() :
            splitted_word[1] = "Street address"

    
        personalInfo[splitted_word[1]] = dictobj[key]

    elif splitted_word[0] == "eeo" :
        eeo[splitted_word[1]] = dictobj[key]
    
    
        
newdict["experienceLevel"] = experienceLevel
newdict["jobTypes"] = jobTypes
newdict["positions"] = positions
newdict["locations"] = locations
newdict["checkboxes"] = checkboxes
newdict["languages"] = languages
newdict["personalInfo"] = personalInfo
newdict["eeo"] = eeo






json_formatted_string = json.dumps(newdict, indent=4)
print(json_formatted_string)
# print(newdict.keys())
