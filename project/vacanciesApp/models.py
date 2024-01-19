from django.db import models


class Main(models.Model):
    image = models.ImageField(upload_to='%d.%m.%Y', blank=False, verbose_name='Изображение')
    first_description = models.TextField(blank=True, verbose_name='Описание вакансии-1')
    second_description = models.TextField(blank=True, verbose_name='Описание вакансии-2')


class Demand(models.Model):
    first_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='Динамика уровня зарплат по годам(все вакансии и Менеджер IT-проекта)')
    first_table = models.TextField(blank=True, verbose_name='Таблица-1')
    second_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                     verbose_name='Динамика количества вакансий по годам(Менеджер IT-проекта)')
    second_table = models.TextField(blank=True, verbose_name='Таблица-2')
    third_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='Динамика количества вакансий по годам(все вакансии)')
    third_table = models.TextField(blank=True, verbose_name='Таблица-3')


class Geography(models.Model):
    first_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='Уровень зарплат по городам(все вакансии и Менеджер IT-проекта)')
    first_table = models.TextField(blank=True, verbose_name='Таблица-1')
    second_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                     verbose_name='Доля вакансий по городам(Менеджер IT-проекта)')
    second_table = models.TextField(blank=True, verbose_name='Таблица-2')
    third_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='Доля вакансий по городам(все вакансии)')
    third_table = models.TextField(blank=True, verbose_name='Таблица-3')


class Skills(models.Model):
    first_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='ТОП-20 навыков по годам(Менеджер IT-проекта)')
    first_table = models.TextField(blank=True, verbose_name='Таблица-1')
    second_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                     verbose_name='ТОП-20 навыков по годам(все вакансии)')
    second_table = models.TextField(blank=True, verbose_name='Таблица-2')


class LastVacancy(models.Model):
    vacancy = models.TextField(blank=False, verbose_name='Название вакансии', max_length=50)


