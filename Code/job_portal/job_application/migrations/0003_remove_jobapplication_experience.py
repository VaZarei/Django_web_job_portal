# Generated by Django 5.1.3 on 2024-12-05 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0002_jobapplication_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='experience',
        ),
    ]