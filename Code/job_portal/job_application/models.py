from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
import os

# Encryption Key (Should be securely stored)
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', Fernet.generate_key())

# Encrypt/Decrypt Functions
cipher = Fernet(ENCRYPTION_KEY)

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(text):
    return cipher.decrypt(text.encode()).decode()

class JobApplication(models.Model):
    
    def __str__(self):
        return f"Username: {self.user.username}"
    
   
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= False)

    username = models.CharField(max_length=150,null=True, blank=True)
    useremail = models.CharField(max_length=150,null=True, blank=True)
  
    """
  
    usernamep = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_job_applications')
    def finduserName():
        #obj = User.objects.get(usernamr= User.username)
        return str(User.username)
        
    usernameo = models.CharField(max_length=130, default=finduserName())
   """
   
   
   
    # def save(self, *args, **kwargs):
    #     if not self.id:  # Check if it's a new instance
    #         obj = User.objects.get(id=1)  # Assuming you only want username for User with ID 1
    #         self.usernamep = str(obj.username)
    #     super().save(*args, **kwargs)
                               
    

    # 1.LinkedIn Credentials
    email = models.EmailField()
    password = models.CharField(max_length=300)

    Choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    disableAntiLock = models.CharField(max_length=10, choices=Choices, default='Yes')
    
    # 2.Job Preferences
    remote = models.CharField(max_length=10, choices=Choices, default='Yes')
    lessthanTenApplicants = models.CharField(max_length=10, choices=Choices, default='No')
    
    
    # 3.Experience Level 
    experienceLevel_internship = models.CharField(max_length=10, choices=Choices, default="Yes")
    experienceLevel_entry = models.CharField(max_length=10, choices=Choices, default="Yes")
    experienceLevel_associate = models.CharField(max_length=10, choices=Choices, default="Yes")
    experienceLevel_midsenior = models.CharField(max_length=10, choices=Choices, default="Yes")
    experienceLevel_director = models.CharField(max_length=10, choices=Choices, default="Yes")
    experienceLevel_executive = models.CharField(max_length=10, choices=Choices, default="Yes")

    
    # 4.Job Type
    jobTypes_fulltime = models.CharField(max_length=10, choices=Choices, default="Yes")
    jobTypes_contract = models.CharField(max_length=10, choices=Choices, default="Yes")
    jobTypes_parttime = models.CharField(max_length=10, choices=Choices, default="Yes")
    jobTypes_temporary = models.CharField(max_length=10, choices=Choices, default="Yes")
    jobTypes_internship = models.CharField(max_length=10, choices=Choices, default="Yes")
    jobTypes_other = models.CharField(max_length=10, choices=Choices, default="Yes")
    jobTypes_volunteer = models.CharField(max_length=10, choices=Choices, default="Yes")


    # 5.Job application Posting Date 
    date = models.CharField(max_length=15, choices=[('all time', 'all time'), ('month', 'month'), ('week', 'week'), ('24 hours', '24 hours')], default="all time")

    # 6.Job Positions is a list, need to write seprate code
    job_positions_1 = models.CharField(max_length=30, null=False, blank= False, default="python developer")
    job_positions_2 = models.CharField(max_length=30, null=False, blank= False, default="digital marketer")
    job_positions_3 = models.CharField(max_length=30, null=True, blank= True)
    job_positions_4 = models.CharField(max_length=30, null=True, blank= True)
    job_positions_5 = models.CharField(max_length=30, null=True, blank= True)
    job_positions_6 = models.CharField(max_length=30, null=True, blank= True)

    # 7.Job Locations is a list, need to write seprate code
    job_locations_1 = models.CharField(max_length=30, null=False, blank=False, default= "England")
    job_locations_2 = models.CharField(max_length=30, null=True, blank=True)
    job_locations_3 = models.CharField(max_length=30, null=True, blank=True)
    job_locations_4 = models.CharField(max_length=30, null=True, blank=True)
    job_locations_5 = models.CharField(max_length=30, null=True, blank=True)
    job_locations_6 = models.CharField(max_length=30, null=True, blank=True)

    # 8.Additional Information
    residentStatus = models.CharField(max_length=10, choices=Choices, default="Yes")
    distance = models.IntegerField(
        choices=[
            (0, 0),
            (5, 5),
            (10, 10),
            (25, 25),
            (50, 50),
            (100, 100),
        ],
        default=25
    )
    # distance = models.IntegerChoices(choices=[(0,0),(5,5),(10,10),(25,25),(50,50),(100,100),], default=25)
    
    # 9.provide the following additional information
    
    uploads_resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    uploads_coverLetter = models.FileField(upload_to='cover_letters/', null=True, blank=True)

    outputFileDirectory = models.CharField(max_length=200, default="write user path/write user path")
    companyBlacklist = models.CharField(max_length=20, null=True)
    titleBlacklist = models.CharField(max_length=20, null=True)
    posterBlacklist = models.CharField(max_length=20, null=True)

    
    # 10.answer the following questions
    checkboxes_driversLicence = models.CharField(max_length=10, choices=Choices)
    checkboxes_requireVisa = models.CharField(max_length=10, choices=Choices)
    checkboxes_legallyAuthorized = models.CharField(max_length=10, choices=Choices, default='yes')
    checkboxes_certifiedProfessional = models.CharField(max_length=10, choices=Choices, default='yes')
    checkboxes_urgentFill = models.CharField(max_length=10, choices=Choices, default='yes')
    checkboxes_commute = models.CharField(max_length=10, choices=Choices, default='yes')
    checkboxes_remote = models.CharField(max_length=10, choices=Choices, default='yes')
    checkboxes_drugTest = models.CharField(max_length=10, choices=Choices, default='yes')
    checkboxes_assessment = models.CharField(max_length=10, choices=Choices, default='yes')
    checkboxes_securityClearance = models.CharField(max_length=10, choices=Choices)
    checkboxes_degreeCompleted  = models.CharField(max_length=40, choices=[('High School Diploma','High School Diploma'), ("Bachelor's Degree","Bachelor's Degree"), ("Master's Degree","Master's Degree"), ("Phd's Degree","Phd's Degree")], default="Bachelor's Degree") # IS a list, need to define
    checkboxes_backgroundCheck = models.CharField(max_length=10, choices=Choices, default='yes')


    # 11.provide the following information
    universityGpa = models.FloatField(null=True, blank=True, default=100)
    salaryMinimum = models.CharField(max_length=20, null=False, blank=False, default='32000')

    languages_1 = models.CharField(max_length=20, null=False, blank=False, default='English')
    languages_2 = models.CharField(max_length=20, null=True, blank=True )
    languages_3 = models.CharField(max_length=20, null=True, blank=True )

    noticePeriod = models.CharField(max_length=5, null=False, blank=False, default='3') # per Week


   




    experience_Experience1 = models.CharField(max_length=35, null=False, blank=False, default='Software Developer : 3')
    experience_Experience2 = models.CharField(max_length=35, null=True, blank=True, default='python : 2')
    experience_Experience3 = models.CharField(max_length=35, null=True, blank=True, default='sql : 8')
    experience_Experience4 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    experience_Experience5 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    experience_Experience6 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    experience_Experience7 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    experience_Experience8 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    experience_Experience9 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    experience_Experience10 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    experience_default = models.CharField(max_length=20,default='default : 1')


    # 12.Personal Information
    personalInfo_Pronouns = models.CharField(max_length=10, choices=[('Mr.','Mr.'), ('Ms.','Ms.'), ('Mx.','Mx.'), ('etc.','etc.')])
    personalInfo_FirstName = models.CharField(max_length=20, null=False, blank=False, default='John')
    personalInfo_lastName = models.CharField(max_length=20, null=False, blank=False, default='Doe')
    personalInfo_PhoneCountryCode = models.CharField(max_length=15, null=False, blank=False, default='+44')
    personalInfo_MobilePhoneNumber = models.CharField(max_length=15, null=False, blank=False, default='+447012345678')
    personalInfo_Streetaddress = models.CharField(max_length=40, null=False, blank=False, default='wimbley street')
    personalInfo_City = models.CharField(max_length=40, null=False, blank=False, default='London')
    personalInfo_State = models.CharField(max_length=40, null=False, blank=False, default='London')
    personalInfo_Zip = models.CharField(max_length=20, null=False, blank=False, default='0WB ACE')
    personalInfo_Linkedin = models.CharField(max_length=80, null=False, blank=False, default='https://www.linkedin.com/in/john-doe/')
    personalInfo_Website = models.URLField(max_length=50, null=True, blank=True, default='https://www.johndoe.com/')
    personalInfo_MessageToManager = models.CharField(max_length=100, null=True, blank=True, default="Hi, I am interested to join your organization. Please have a look at my resume. Thank you.")

    #13. provide the following information (for US-based jobs)
    eeo_gender = models.CharField(max_length=30, choices=[('Male','Male'), ('Female','Female'), ('Non-binary.','Non-binary'), ('Other','Other')], null=True, default=None)
    eeo_race = models.CharField(max_length=20, null=True, blank=False, default="null")
    eeo_veteran = models.CharField(max_length=10, choices=Choices, default="Yes")
    eeo_disability = models.CharField(max_length=10, choices=Choices, default="no")
    eeo_citizenship = models.CharField(max_length=10, choices=Choices, default='yes')
    eeo_clearance = models.CharField(max_length=10, choices=Choices, default="Yes")


    



    



    

    
    def get_linkedin_password(self):
        return decrypt(self.password)
