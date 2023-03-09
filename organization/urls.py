from django.urls import path
from .views import NewOrgView, Pie, SurveyView
from . import views


app_name = 'organization'

urlpatterns = [
    path('', views.index, name = 'index'),
    path("new_organization/", NewOrgView.as_view(), name = 'neworg'),
    path('success/', views.success, name = 'success'),
    path('orgs/', views.orgs, name = 'organizations'),
    path('orgs/<int:org_id>', views.orgpage, name ='orgpage'),
    path('pie/', Pie.as_view(), name = 'pie'),
    path('survey/', SurveyView.as_view(), name="survey"),
]
