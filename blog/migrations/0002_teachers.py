# Generated by Django 4.0.2 on 2022-02-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('sohasi', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('text', models.TextField()),
            ],
        ),
    ]
