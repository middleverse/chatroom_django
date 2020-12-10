from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # home page
    path('<str:room_name>/', views.room, name='room'), # chat room
]

