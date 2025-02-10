from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('drakeRoom/', views.DrakeRoom, name="Drake's room")
]