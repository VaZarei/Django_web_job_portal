import os
import django
import json
############################################## python -m backend.dbExtract.py #######################################
# Set the Django project path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal.settings')
django.setup()

# Now you can import models
from job_application.models import JobApplication


obj = JobApplication.objects.get(id=2)
print(type(obj.__dict__))
dictobj = obj.__dict__

def cleaningElement(str):
    """ a function to convert yes or no to boolean"""

    if str == "Yes":
            str=bool(True)
            return str  
    elif str == "No":
            str=bool(False)
            return str
    else:
        return str
    

newdict = {}
experienceLevel = {}
jobTypes = {}
positions = []
locations = []
uploads = {}
checkboxes= {}
languages = {}
experience = []
personalInfo = {}
eeo = {}



blockwords = ["_state", "user_id" ]
for key in dictobj.keys():
    
    if blockwords[0] == key.lower() or blockwords[1] == key.lower():
        continue
        
    splitted_word = key.split('_')
    

    if len(splitted_word)==1 :
        if "date".lower() in splitted_word[0].lower():
            newdict[splitted_word[0]] = {dictobj[key]: bool(True)}
            continue

        newdict[splitted_word[0]] = cleaningElement(dictobj[key])

#---------------------------------------------------------------------------- experienceLevel
    elif splitted_word[0] == "experienceLevel" :
        if "midsenior".lower() in splitted_word[1].lower():
            splitted_word[1] = "mid-senior level"


        experienceLevel[splitted_word[1]] = cleaningElement(dictobj[key])
#---------------------------------------------------------------------------- jobTypes
    elif splitted_word[0] == "jobTypes" :
        if "fulltime".lower() in splitted_word[1].lower() :
            splitted_word[1] = "full-time"
        
        if "parttime".lower() in splitted_word[1].lower() :
            splitted_word[1] = "part-time"

        jobTypes[splitted_word[1]] = cleaningElement(dictobj[key])
#---------------------------------------------------------------------------- Positions
    elif splitted_word[1] == "positions" : 
        if dictobj[key] is not None:        
           positions.append(dictobj[key] )
#---------------------------------------------------------------------------- locations
    elif splitted_word[1] == "locations" :        
        if dictobj[key] is not None:
           locations.append(cleaningElement(dictobj[key]))
        
#---------------------------------------------------------------------------- uploads
    elif splitted_word[0] == "uploads" :        
        uploads[splitted_word[1]] = dictobj[key]



#---------------------------------------------------------------------------- checkboxes
    elif splitted_word[0] == "checkboxes" :
        if "degreeCompleted".lower() in splitted_word[1].lower() :
            checkboxes[splitted_word[1]] = [dictobj[key]]
            continue
        checkboxes[splitted_word[1]] = cleaningElement(dictobj[key])

#---------------------------------------------------------------------------- language
    elif splitted_word[0] == "languages" :
        languages[dictobj[key]] = "Native or bilingual"   

#---------------------------------------------------------------------------- experience
    elif splitted_word[0] == "experience" :
        if dictobj[key] is not None:
            experience.append(str(dictobj[key]))


#---------------------------------------------------------------------------- personalInfo 
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
#---------------------------------------------------------------------------- eeo
    elif splitted_word[0] == "eeo" :
        eeo[splitted_word[1]] = cleaningElement(dictobj[key])
    
    
        
newdict["experienceLevel"] = experienceLevel
newdict["jobTypes"] = jobTypes
newdict["positions"] = positions
newdict["locations"] = locations
newdict["uploads"] = uploads
newdict["checkboxes"] = checkboxes
newdict["languages"] = languages
newdict["experience"] = experience
newdict["personalInfo"] = personalInfo
newdict["eeo"] = eeo








json_formatted_string = json.dumps(newdict, indent=4)
print(json_formatted_string)
# print(newdict.keys())
