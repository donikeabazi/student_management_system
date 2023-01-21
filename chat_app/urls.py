from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user/<str:id>', views.profile, name="user-profile"),
    path('room/add', views.createRoom, name="add-room"),
    path('room/<str:id>', views.room, name="room"),
    path('room/<str:id>/update', views.updateRoom, name="update-room"),
    path('room/<str:id>/delete', views.deleteRoom, name="delete-room"),
    path('message/<str:id>/delete', views.deleteMessage, name="delete-message"),
]
