from django.urls import path, include
from .views import RegisterView
from . import views


app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("", include("django.contrib.auth.urls")),
    path('edit_profile/', views.update_user_profile, name='edit_profile'),
]

