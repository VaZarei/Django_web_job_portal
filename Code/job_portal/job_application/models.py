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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # 1.LinkedIn Credentials
    linkedin_email = models.EmailField()
    linkedin_password_encrypted = models.TextField()
    
    
    # 2.Job Preferences
    remote_jobs = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    fewer_applicants = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default='No')
    
    # 3.Experience Level 
    experience_internship = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    experience_entry = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    experience_associate = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    experience_mid_Senior = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    experience_director = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    experience_executive = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")

    
    # 4.Job Type
    jobtype_fulltime = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    jobtype_contract = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    jobtype_parttime = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    jobtype_temprory = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    jobtype_internship = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")
    jobtype_volunteer = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')], default="Yes")


    # 5.Job application Posting Date 
    Posting_Date = models.CharField(max_length=15, choices=[('All_Time', 'All_Time'), ('month', 'month'), ('week', 'week'), ('24_hours', '24_hours')], default="All_Time")

    # 6.Job Positions
    job_position_1 = models.CharField(max_length=30, null=False, blank= False, default="python developer")
    job_position_2 = models.CharField(max_length=30, null=False, blank= False, default="digital marketer")
    job_position_3 = models.CharField(max_length=30, null=True, blank= True)
    job_position_4 = models.CharField(max_length=30, null=True, blank= True)
    job_position_5 = models.CharField(max_length=30, null=True, blank= True)
    job_position_6 = models.CharField(max_length=30, null=True, blank= True)

    # 7.Job Locations
    job_location_1 = models.CharField(max_length=30, null=False, blank=False, default= "England")
    job_location_2 = models.CharField(max_length=30, null=True, blank=True)
    job_location_3 = models.CharField(max_length=30, null=True, blank=True)
    job_location_4 = models.CharField(max_length=30, null=True, blank=True)
    job_location_5 = models.CharField(max_length=30, null=True, blank=True)
    job_location_6 = models.CharField(max_length=30, null=True, blank=True)

    # 8.Additional Information
    resident_status = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default="Yes")
    distance_from_job_location = models.CharField(max_length=10, choices=[('0','0'),('5','5'),('10','10'),('25','25'),('50','50'),('100','100'),], default='25')

    # 9.provide the following additional information
    
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='cover_letters/', null=True, blank=True)
    
    # 10.answer the following questions
    has_driver_license = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')])
    requires_sponsorship = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')])
    authorized_to_work = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    necessary_licenses = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    start_immediately = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    comfortable_with_commuting = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    comfortable_with_remote_work = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    drug_test = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    complete_an_assessment = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    security_clearance = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')])
    completed_Degree  = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    background_check = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')


    # 11.provide the following information
    University_gpa = models.CharField(max_length=30, null=True, blank=True, default='A')
    Minimum_Salary_Expectation = models.CharField(max_length=20, null=False, blank=False, default='32000')

    language_1 = models.CharField(max_length=20, null=False, blank=False, default='English')
    language_2 = models.CharField(max_length=20, null=True, blank=True )
    language_3 = models.CharField(max_length=20, null=True, blank=True )

    Notice_Period = models.CharField(max_length=5, null=False, blank=False, default='3') # per Week
    Years_of_Experience_1 = models.CharField(max_length=35, null=False, blank=False, default='Software Developer : 3')
    Years_of_Experience_2 = models.CharField(max_length=35, null=True, blank=True, default='python : 2')
    Years_of_Experience_3 = models.CharField(max_length=35, null=True, blank=True, default='sql : 8')
    Years_of_Experience_4 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    Years_of_Experience_5 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    Years_of_Experience_6 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    Years_of_Experience_7 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    Years_of_Experience_8 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    Years_of_Experience_9 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')
    Years_of_Experience_10 = models.CharField(max_length=35, null=True, blank=True, default='aws : 3')


    # 12.Personal Information
    pronouns = models.CharField(max_length=10, choices=[('Mr.','Mr.'), ('Ms.','Ms.'), ('Mx.','Mx.'), ('etc.','etc.')])
    first_Name = models.CharField(max_length=20, null=False, blank=False, default='John')
    last_Name = models.CharField(max_length=20, null=False, blank=False, default='Doe')
    phone_country_code = models.CharField(max_length=15, null=False, blank=False, default='+44')
    phone_number = models.CharField(max_length=15, null=False, blank=False, default='+447012345678')
    street_address = models.CharField(max_length=40, null=False, blank=False, default='wimbley street')
    city = models.CharField(max_length=40, null=False, blank=False, default='London')
    state = models.CharField(max_length=40, null=False, blank=False, default='London')
    zip_code = models.CharField(max_length=20, null=False, blank=False, default='0WB ACE')
    Linkedin_Profile = models.CharField(max_length=80, null=False, blank=False, default='https://www.linkedin.com/in/john-doe/')
    website = models.CharField(max_length=50, null=True, blank=True, default='https://www.johndoe.com/')
    message_to_hire = models.CharField(max_length=100, null=True, blank=True, default="Hi, I am interested to join your organization. Please have a look at my resume. Thank you.")

    #13. provide the following information (for US-based jobs)
    pronouns_us = models.CharField(max_length=30, choices=[('Male','Male'), ('Female','Female'), ('Non-binary.','Non-binary'), ('Other','Other')], null=True, default=None)
    race = models.CharField(max_length=20, null=False, blank=False, default='none')
    veteran_status = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default="Yes")
    disability_status = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default="no")
    citizenship = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default='yes')
    security_clearance_us = models.CharField(max_length=10, choices=[('yes','yes'), ('no','no')], default="Yes")



    



    



    
    def save(self, *args, **kwargs):
        if not self.pk:  # Encrypt LinkedIn password on first save
            self.linkedin_password_encrypted = encrypt(self.linkedin_password_encrypted)
        super().save(*args, **kwargs)
    
    def get_linkedin_password(self):
        return decrypt(self.linkedin_password_encrypted)
