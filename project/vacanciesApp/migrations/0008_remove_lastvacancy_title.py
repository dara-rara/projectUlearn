# Generated by Django 4.2.9 on 2024-01-18 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacanciesApp', '0007_remove_main_description_main_first_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastvacancy',
            name='title',
        ),
    ]
