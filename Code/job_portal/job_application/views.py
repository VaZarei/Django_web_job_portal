from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .models import JobApplication
from confluent_kafka import Producer
import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Kafka producer configuration
producer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'django-producer'
}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

@login_required
@login_required
def job_application_view(request):
    """Handles job application form submission and sends data to Kafka."""
    try:
        job_application, created = JobApplication.objects.get_or_create(user=request.user)
    except ObjectDoesNotExist:
        job_application = JobApplication.objects.create(user=request.user)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=job_application)
        if form.is_valid():
            form.save()
            print("Form saved successfully!")  # Debug statement
            return redirect('home')  # Ensure this is the correct URL name
        else:
            print("Form validation failed.")  # Debug statement
    else:
        form = JobApplicationForm(instance=job_application)
    
    return render(request, 'job_application/form.html', {'form': form})

### Profile View

@login_required
def profile_view(request):
    """Displays the user's profile with their job application data."""
    try:
        job_application = request.user.jobapplication
    except JobApplication.DoesNotExist:
        job_application = None
    return render(request, 'job_application/profile.html', {'job_application': job_application})

### Edit Job Application View

@login_required
def edit_job_application(request):
    """Allows users to edit their job application form."""
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=request.user.jobapplication)
        if form.is_valid():
            form.save()
            return redirect('job_application:profile')
    else:
        form = JobApplicationForm(instance=request.user.jobapplication)
    return render(request, 'job_application/edit_form.html', {'form': form})
