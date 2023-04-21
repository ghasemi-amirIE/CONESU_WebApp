from django.urls import path, include
from .views import NewOrgView, Pie, Landing
from . import views


app_name = 'organization'

urlpatterns = [
    path('', views.landing_page, name = 'index'),
    path("new_organization/", NewOrgView.as_view(), name = 'neworg'),
    path('success/', views.success, name = 'success'),
    path('orgs/', views.orgs, name = 'organizations'),
    path('orgs/<int:org_id>', views.orgpage, name ='orgpage'),
    path('pie/', Pie.as_view(), name = 'pie'),
    path('survey/', views.survey, name="survey"),
    path('profile/', views.profile, name = 'profile'),
    path('landing/', Landing.as_view(), name='test-landing-page'),
    path('info_pages/', include('info_pages.urls')),
]
