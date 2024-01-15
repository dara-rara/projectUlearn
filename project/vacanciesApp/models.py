from django.db import models


class Navigation(models.Model):
    image = models.ImageField(upload_to='%d.%m.%Y', blank=False, verbose_name='Иконка')
    title = models.CharField(max_length=50, verbose_name='Название вакансии')
    first_link = models.CharField(max_length=50, verbose_name='Первый пункт')
    second_link = models.CharField(max_length=50, verbose_name='Второй пункт')
    third_link = models.CharField(max_length=50, verbose_name='Третий пункт')
    fourth_link = models.CharField(max_length=50, verbose_name='Четвертый пункт')
    fifth_link = models.CharField(max_length=50, verbose_name='Пятый пункт')
    author = models.CharField(max_length=50, verbose_name='Автор')


class Main(models.Model):
    image = models.ImageField(upload_to='%d.%m.%Y', blank=False, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание вакансии')


class Demand(models.Model):
    first_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='Динамика уровня зарплат по годам(все вакансии и Менеджер IT-проекта')
    second_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                     verbose_name='Динамика количества вакансий по годам(Менеджер IT-проекта)')
    third_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='Динамика количества вакансий по годам(все вакансии)')
    table = models.TextField(blank=True, verbose_name='Таблица')


class Geography(models.Model):
    first_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='Уровень зарплат по городам(все вакансии и Менеджер IT-проекта')
    second_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                     verbose_name='Доля вакансий по городам(Менеджер IT-проекта)')
    third_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='Доля вакансий по городам(все вакансии)')
    table = models.TextField(blank=True, verbose_name='Таблица')


class Skills(models.Model):
    first_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                    verbose_name='ТОП-20 навыков по годам(Менеджер IT-проекта')
    second_graph = models.ImageField(upload_to='%d.%m.%Y', blank=False,
                                     verbose_name='ТОП-20 навыков по годам(все вакансии)')
    table = models.TextField(blank=True, verbose_name='Таблица')


class LastVacancy(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок статистика')
    vacancy = models.CharField(blank=False, verbose_name='Название вакансии', max_length=50)


