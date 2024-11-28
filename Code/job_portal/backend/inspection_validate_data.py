import yaml
from validate_email import validate_email
import json



def validate_yaml():
    with open("F:/jobBot/Code/job_portal/backend/config.yaml", 'r') as stream:
        
        try:
            parameters = yaml.safe_load(stream)
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

para = validate_yaml()


json_formatet_para = json.dumps(para, indent=4)
print(json_formatet_para)

