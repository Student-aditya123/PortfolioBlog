from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project_list/', views.project_list, name='projects'),
    path('contact/', views.contact, name='contact'),
]

