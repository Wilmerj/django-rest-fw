from rest_framework.response import Response
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatientView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

