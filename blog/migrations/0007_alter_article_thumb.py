# Generated by Django 4.0.3 on 2022-03-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_remove_application_course_delete_teachers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]