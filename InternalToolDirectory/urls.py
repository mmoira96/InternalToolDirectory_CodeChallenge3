from django.contrib import admin
from django.urls import path
from codechallenge3 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tools/", views.tool_list, name="tools"),
]
