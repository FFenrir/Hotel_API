from django.urls import path

from .views import ReportListView,ReprtDetailView



urlpatterns = [
    path('reports/',ReportListView.as_view()),
    path('reports/<int:pk>',ReprtDetailView.as_view()),
]