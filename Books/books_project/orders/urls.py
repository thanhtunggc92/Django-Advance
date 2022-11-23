from django.urls import path
from .views import OrderPageView


urlpatterns=[
    path('',OrderPageView,name='orders'),
]