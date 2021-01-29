from django.contrib import admin
from django.urls import path, include, re_path
from news import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r"^api/topHeadLines", views.topHeadLines.as_view()),
    re_path(r"^api/category/", views.Categories.as_view()),


]
