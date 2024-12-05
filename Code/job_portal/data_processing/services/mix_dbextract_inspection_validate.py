import yaml
from validate_email import validate_email
import json

import yaml
import os
import django


############################################## python -m data_processing.services.mix_dbextract_inspection_validate.py  #######################################

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal.settings')
django.setup()


from job_application.models import JobApplication


def dbExtract(model_name,username):
    
    obj = model_name.objects.get(username=username)
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
    experience = {}
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
                exp = (str(dictobj[key]).split(':'))
                exp[0] = str(exp[0]).strip()
                experience[exp[0]] = int(exp[1])


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


    return newdict

def validate_extracted_dict(dict):
    
        
    try:
        parameters = dict
        print(type(parameters), "*"*100)
    except yaml.YAMLError as exc:
        raise exc

    
    mandatory_params = ['email',
                        'password',
                        'disableAntiLock',
                        'remote',
                        'lessthanTenApplicants',
                        'experienceLevel',
                        'jobTypes',
                        'date',
                        'positions',
                        'locations',
                        'residentStatus',
                        'distance',
                        'outputFileDirectory',
                        'checkboxes',
                        'universityGpa',
                        'languages',
                        'experience',
                        'personalInfo',
                        'eeo',
                        'uploads']

    for mandatory_param in mandatory_params:
        if mandatory_param not in parameters:
            raise Exception(mandatory_param + ' is not defined in the config.yaml file!')

    assert validate_email(parameters['email'])
    assert len(str(parameters['password'])) > 0
    assert isinstance(parameters['disableAntiLock'], bool)
    assert isinstance(parameters['remote'], bool)
    assert isinstance(parameters['lessthanTenApplicants'], bool)
    assert isinstance(parameters['residentStatus'], bool)
    assert len(parameters['experienceLevel']) > 0
    experience_level = parameters.get('experienceLevel', [])
    at_least_one_experience = False

    for key in experience_level.keys():
        if experience_level[key]:
            at_least_one_experience = True
    assert at_least_one_experience

    assert len(parameters['jobTypes']) > 0
    job_types = parameters.get('jobTypes', [])
    at_least_one_job_type = False
    for key in job_types.keys():
        if job_types[key]:
            at_least_one_job_type = True

    assert at_least_one_job_type
    assert len(parameters['date']) > 0
    date = parameters.get('date', [])
    at_least_one_date = False

    for key in date.keys():
        if date[key]:
            at_least_one_date = True
    assert at_least_one_date

    approved_distances = {0, 5, 10, 25, 50, 100}
    assert parameters['distance'] in approved_distances
    assert len(parameters['positions']) > 0
    assert len(parameters['locations']) > 0
    assert len(parameters['uploads']) >= 1 and 'resume' in parameters['uploads']
    assert len(parameters['checkboxes']) > 0

    checkboxes = parameters.get('checkboxes', [])
    assert isinstance(checkboxes['driversLicence'], bool)
    assert isinstance(checkboxes['requireVisa'], bool)
    assert isinstance(checkboxes['legallyAuthorized'], bool)
    assert isinstance(checkboxes['certifiedProfessional'], bool)
    assert isinstance(checkboxes['urgentFill'], bool)
    assert isinstance(checkboxes['commute'], bool)
    assert isinstance(checkboxes['backgroundCheck'], bool)
    assert isinstance(checkboxes['securityClearance'], bool)
    assert 'degreeCompleted' in checkboxes
    assert isinstance(parameters['universityGpa'], (int, float))

    languages = parameters.get('languages', [])
    language_types = {'none', 'conversational', 'professional', 'native or bilingual'}
    for language in languages:
        assert languages[language].lower() in language_types

    experience = parameters.get('experience', [])
    for tech in experience:
        assert isinstance(experience[tech], int)
    assert 'default' in experience

    assert len(parameters['personalInfo'])
    personal_info = parameters.get('personalInfo', [])
    for info in personal_info:
        assert personal_info[info] != ''

    assert len(parameters['eeo'])
    eeo = parameters.get('eeo', [])
    for survey_question in eeo:
        assert eeo[survey_question] != ''

    return parameters

para = validate_extracted_dict(dbExtract(JobApplication,'vahidz'))


json_formatet_para = json.dumps(para, indent=4)
print(json_formatet_para)



    #---------------------------------------------------------------------------- Save as a file

import os
import yaml

# Your dictionary variable


# Define the directory and file name
directory = os.path.join("data_processing", "services", "yamlfiles")
file_name = "data.yaml"

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Define the full file path
file_path = os.path.join(directory, file_name)

# Save the dictionary as a YAML file
with open(file_path, "w") as yaml_file:
    yaml.dump(json_formatet_para, yaml_file, default_flow_style=False)

print(f"File saved at: {file_path}")
