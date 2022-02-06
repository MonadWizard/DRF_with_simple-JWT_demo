from django.urls import path
from . import views


urlpatterns = [
    path('viewuser', views.viewUser),


]
