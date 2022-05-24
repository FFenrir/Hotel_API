from django.urls import path

from .views import RoomListView,RoomDetailView

urlpatterns = [
    path('rooms/',RoomListView.as_view()),
    path('rooms/<int:pk>',RoomDetailView.as_view()),
]