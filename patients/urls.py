from patients.views import ListPatientsView, DetailPatientView
from django.urls import path

urlpatterns = [
    path('patients/', ListPatientsView.as_view()),
    path('patients/<int:pk>/', DetailPatientView.as_view()),
]
