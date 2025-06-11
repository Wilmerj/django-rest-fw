from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Doctor, Department
from .serializers import DoctorSerializer, DepartmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    """
    List all doctors or create a new doctor
    """
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    @action(methods=['post'], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response("Doctor is now on vacation", status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response("Doctor is now back from vacation", status=status.HTTP_200_OK)

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    List all departments or create a new department
    """
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()