from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('get_customer/', views.customer_data_view),
]
