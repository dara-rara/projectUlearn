# Generated by Django 4.2.9 on 2024-01-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacanciesApp', '0005_remove_demand_table_demand_first_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geography',
            name='table',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='table',
        ),
        migrations.AddField(
            model_name='geography',
            name='first_table',
            field=models.TextField(blank=True, verbose_name='Таблица-1'),
        ),
        migrations.AddField(
            model_name='geography',
            name='second_table',
            field=models.TextField(blank=True, verbose_name='Таблица-2'),
        ),
        migrations.AddField(
            model_name='geography',
            name='third_table',
            field=models.TextField(blank=True, verbose_name='Таблица-3'),
        ),
        migrations.AddField(
            model_name='skills',
            name='first_table',
            field=models.TextField(blank=True, verbose_name='Таблица-1'),
        ),
        migrations.AddField(
            model_name='skills',
            name='second_table',
            field=models.TextField(blank=True, verbose_name='Таблица-2'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='second_table',
            field=models.TextField(blank=True, verbose_name='Таблица-2'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='third_table',
            field=models.TextField(blank=True, verbose_name='Таблица-3'),
        ),
    ]
