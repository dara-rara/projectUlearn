from datetime import datetime
import re
import requests
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_main(request):
    return render(request, 'main.html', {'content': Main.objects.all()})


@csrf_exempt
def get_demand(request):
    return render(request, 'demand.html', {'content': Demand.objects.all()})


@csrf_exempt
def get_geography(request):
    return render(request, 'geography.html', {'content': Geography.objects.all()})


@csrf_exempt
def get_skills(request):
    return render(request, 'skills.html', {'content': Skills.objects.all()})


@csrf_exempt
def get_last_vacancies(request):
    name = LastVacancy.objects().all()
    if name:
        apiHH = ApiHH(name.last().vacancy)
        date = datetime.now().strftime('%Y-%m-%d')
        return render(request, 'last_vacancies.html', {'content': apiHH.get_vacancies(date, 10)})
    else:
        return render(request, 'last_vacancies.html', {'content': 'Параметр не задан!'})


class ApiHH:

    def __init__(self, name_vac: str):
        self.name_vac = name_vac

    def get_vacancies(self, date: str, count: int):
        dic_currency = {'AZN': 'Манаты',
                        'BYR': 'Белорусские рубли',
                        'EUR': 'Евро',
                        'GEL': 'Грузинский лари',
                        'KGS': 'Киргизский сом',
                        'KZT': 'Тенге',
                        'RUR': 'Рубли',
                        'UAH': 'Гривны',
                        'USD': 'Доллары',
                        'UZS': 'Узбекский сум'}

        response = requests.get('https://api.hh.ru/vacancies', params={
            'text': self.name_vac,
            'specialization': 1,
            'date_from': f'{date}T00:00:00',
            'date_to': f'{date}T23:00:00',
            'per_page': count,
            'page': 1
        }).json()

        vacancies = response.get("items", [])
        result = []
        for vacancy in vacancies:
            data = requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()

            if data['salary']['from'] and data['salary']['to']:
                description = ' '.join(re.sub(re.compile('<.*?>'), '', data['description']).strip().split())
                description = description[:300] + '...' if len(description) >= 300 else description
                key_skills = ', '.join([row['name'] for row in data['key_skills']]) if data['key_skills'] else '-'
                result.append({
                    'name': data['name'],
                    'description': description,
                    'key_skills': key_skills,
                    'employer': data['employer']['name'],
                    'salary': f"{data['salary']['from']} - {data['salary']['to']} "
                              f"{dic_currency.get(data['salary']['currency'])}",
                    'area': data['area']['name'],
                    'published_at': data['published_at'][:10],
                })
        return result
