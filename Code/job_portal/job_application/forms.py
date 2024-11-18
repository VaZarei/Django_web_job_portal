from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'linkedin_email', 'linkedin_password_encrypted',
            'remote_jobs', 'fewer_applicants', 'experience_level',
            'job_type', 'job_posting_date', 'job_positions',
            'job_locations', 'resident_status', 'distance_from_job_location',
            'resume', 'cover_letter', 'has_driver_license',
            'requires_sponsorship', 'pronouns', 'first_name', 'last_name',
            'phone_number', 'linkedin_profile'
        ]
        widgets = {
            'linkedin_password_encrypted': forms.PasswordInput(),
        }
