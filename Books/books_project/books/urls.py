from django.urls import path
from . import views


urlpatterns=[
    path('detail/',views.BookView,name='book-list' ),
    path('detail/<str:pk>/',views.BookDetail,name='book-detail')

]