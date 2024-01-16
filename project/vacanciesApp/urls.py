from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_main, name='main'),
    path('demand/', views.get_demand, name='demand'),
    path('geography/', views.get_geography, name='geography'),
    path('skills/', views.get_skills, name='skills')
    #path('last-vac')
]
