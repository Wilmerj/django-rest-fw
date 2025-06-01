from patients.views import list_patients, detail_patient
from django.urls import path

urlpatterns = [
    path('patients/', list_patients),
    path('patients/<int:pk>/', detail_patient),
]
