# Generated by Django 5.1.3 on 2024-11-19 15:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_email', models.EmailField(max_length=254)),
                ('linkedin_password_encrypted', models.TextField()),
                ('remote_jobs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('fewer_applicants', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('experience_internship', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('experience_entry', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('experience_associate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('experience_mid_Senior', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('experience_director', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('experience_executive', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('jobtype_fulltime', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('jobtype_contract', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('jobtype_parttime', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('jobtype_temprory', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('jobtype_internship', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('jobtype_volunteer', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('Posting_Date', models.CharField(choices=[('All_Time', 'All_Time'), ('month', 'month'), ('week', 'week'), ('24_hours', '24_hours')], default='All_Time', max_length=15)),
                ('job_position_1', models.TextField(default='python developer', max_length=30)),
                ('job_position_2', models.TextField(default='digital marketer', max_length=30)),
                ('job_position_3', models.TextField(blank=True, max_length=30, null=True)),
                ('job_position_4', models.TextField(blank=True, max_length=30, null=True)),
                ('job_position_5', models.TextField(blank=True, max_length=30, null=True)),
                ('job_position_6', models.TextField(blank=True, max_length=30, null=True)),
                ('job_location_1', models.TextField(default='England', max_length=30)),
                ('job_location_2', models.TextField(blank=True, max_length=30, null=True)),
                ('job_location_3', models.TextField(blank=True, max_length=30, null=True)),
                ('job_location_4', models.TextField(blank=True, max_length=30, null=True)),
                ('job_location_5', models.TextField(blank=True, max_length=30, null=True)),
                ('job_location_6', models.TextField(blank=True, max_length=30, null=True)),
                ('resident_status', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='Yes', max_length=10)),
                ('distance_from_job_location', models.CharField(choices=[('0', '0'), ('5', '5'), ('10', '10'), ('25', '25'), ('50', '50'), ('100', '100')], max_length=10)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to='cover_letters/')),
                ('has_driver_license', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('requires_sponsorship', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('authorized_to_work', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('necessary_licenses', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('start_immediately', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('comfortable_with_commuting', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('comfortable_with_remote_work', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('drug_test', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('complete_an_assessment', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('completed_Degree', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('background_check', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('University_gpa', models.TextField(blank=True, default='A', max_length=30, null=True)),
                ('Minimum_Salary_Expectation', models.TextField(default='32000', max_length=20)),
                ('language_1', models.TextField(default='English', max_length=20)),
                ('language_2', models.TextField(blank=True, max_length=20, null=True)),
                ('language_3', models.TextField(blank=True, max_length=20, null=True)),
                ('Notice_Period', models.TextField(default='3', max_length=5)),
                ('Years_of_Experience_1', models.TextField(default='Software Developer : 3', max_length=35)),
                ('Years_of_Experience_2', models.TextField(blank=True, default='python : 2', max_length=35, null=True)),
                ('Years_of_Experience_3', models.TextField(blank=True, default='sql : 8', max_length=35, null=True)),
                ('Years_of_Experience_4', models.TextField(blank=True, default='aws : 3', max_length=35, null=True)),
                ('first_Name', models.TextField(default='John', max_length=20)),
                ('last_Name', models.TextField(default='Doe', max_length=20)),
                ('phone_number', models.TextField(default='+447012345678', max_length=30)),
                ('street_address', models.TextField(default='wimbley street', max_length=40)),
                ('city', models.TextField(default='London', max_length=40)),
                ('state', models.TextField(default='London', max_length=40)),
                ('zip_code', models.TextField(default='0WB ACE', max_length=20)),
                ('Linkedin_Profile', models.TextField(default='https://www.linkedin.com/in/john-doe/', max_length=80)),
                ('website', models.TextField(blank=True, default='https://www.johndoe.com/', max_length=50, null=True)),
                ('message_to_hire', models.CharField(blank=True, default='Doe', max_length=100, null=True)),
                ('pronouns', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-binary.', 'Non-binary'), ('Other', 'Other')], max_length=30)),
                ('race', models.TextField(default='none', max_length=20)),
                ('veteran_status', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='Yes', max_length=10)),
                ('disability_status', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10)),
                ('citizenship', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('security_clearance', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='Yes', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
