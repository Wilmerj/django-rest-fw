from .serializers import PatientSerializer
from .models import Patient
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class ListPatientsView(ListAPIView, CreateAPIView):
    """
    List all patients or create a new patient
    """
    allowed_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatientView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

