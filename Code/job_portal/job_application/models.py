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
    
    # LinkedIn Credentials
    linkedin_email = models.EmailField()
    linkedin_password_encrypted = models.TextField()
    
    # Job Preferences
    remote_jobs = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])
    fewer_applicants = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])
    experience_level = models.JSONField(default=dict)
    job_type = models.JSONField(default=dict)
    job_posting_date = models.CharField(max_length=20, default='All Time')
    job_positions = models.JSONField(default=list)
    job_locations = models.JSONField(default=list)
    
    # Additional Info
    resident_status = models.BooleanField(default=True)
    distance_from_job_location = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='cover_letters/', null=True, blank=True)
    
    # Extra Questions
    has_driver_license = models.BooleanField(default=True)
    requires_sponsorship = models.BooleanField(default=False)
    
    # Personal Info
    pronouns = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    linkedin_profile = models.URLField()
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Encrypt LinkedIn password on first save
            self.linkedin_password_encrypted = encrypt(self.linkedin_password_encrypted)
        super().save(*args, **kwargs)
    
    def get_linkedin_password(self):
        return decrypt(self.linkedin_password_encrypted)
