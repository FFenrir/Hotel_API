from django.urls import path

from .views import ClienrListView,ClientDetailView



urlpatterns = [
    path('clients/',ClienrListView.as_view()),
    path('clients/<int:pk>',ClientDetailView.as_view()),
]