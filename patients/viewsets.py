from rest_framework import viewsets

from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    """
    List all patients or create a new patient
    """
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()