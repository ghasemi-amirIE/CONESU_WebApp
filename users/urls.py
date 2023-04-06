from django.urls import path, include
from .views import RegisterView


app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("", include("django.contrib.auth.urls")),
]

