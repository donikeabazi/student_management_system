from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('room/add', views.createRoom, name="add-room"),
    path('room/<str:id>', views.room, name="room"),
    path('room/<str:id>/update', views.updateRoom, name="update-room"),
    path('room/<str:id>/delete', views.deleteRoom, name="delete-room"),
]
