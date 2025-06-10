from rest_framework import viewsets

from .models import Doctor, Department
from .serializers import DoctorSerializer, DepartmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    """
    List all doctors or create a new doctor
    """
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    List all departments or create a new department
    """
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()