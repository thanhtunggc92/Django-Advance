from pydoc import visiblename
from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomePage,name='home'),
    path('about/',views.AboutView, name='about')
]