# Generated by Django 4.0.2 on 2022-03-07 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_application_course_application_client_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='Course',
            new_name='course',
        ),
    ]
