# Generated by Django 5.1.3 on 2024-12-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0003_remove_jobapplication_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='experience_default',
            field=models.CharField(default='default : 1', max_length=20),
        ),
    ]