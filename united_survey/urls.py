
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("organization.urls")),
    path("users/", include("users.urls")),
    path("", include("info_pages.urls")),
]
