# Generated by Django 5.1.3 on 2024-11-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0006_alter_jobapplication_linkedin_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='pronouns_us',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-binary.', 'Non-binary'), ('Other', 'Other')], default=None, max_length=30, null=True),
        ),
    ]
