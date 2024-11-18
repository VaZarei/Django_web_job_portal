from django.urls import path
from . import views

app_name = 'job_application'

urlpatterns = [
    # Route for the job application form
    path('form/', views.job_application_view, name='job_form'),
    
    # Route to view the user's profile (with filled form data)
    path('profile/', views.profile_view, name='profile'),
    
    # Route for users to edit their job application form
    path('edit/', views.edit_job_application, name='edit_form'),

    # Additional routes can be added as needed
]
