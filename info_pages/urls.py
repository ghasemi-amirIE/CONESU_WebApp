from django.urls import path
from . import views

app_name = 'info_pages'

urlpatterns = [
    path('project/<str:project_name>/', views.project, name='project'),
    path('resources/', views.resources, name='resources'),
]