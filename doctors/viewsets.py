from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Doctor, Department
from .serializers import DoctorSerializer, DepartmentSerializer
from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment
from .permissions import IsDoctor


class DoctorViewSet(viewsets.ModelViewSet):
    """
    List all doctors or create a new doctor
    """

    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]

    @action(methods=["post"], detail=True, url_path="set-on-vacation")
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response("Doctor is now on vacation", status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True, url_path="set-off-vacation")
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response("Doctor is now back from vacation", status=status.HTTP_200_OK)

    @action(
        methods=["get", "post", "delete"],
        detail=True,
        serializer_class=AppointmentSerializer,
        url_path="appointments(?:/(?P<appointment_id>[^/.]+))?",
    )
    def appointments(self, request, pk, appointment_id=None):
        doctor = self.get_object()
        if request.method == "POST":
            data = request.data.copy()
            data["doctor"] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == "GET":
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        if request.method == "DELETE":
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return Response(
                {"message": "Appointment deleted"}, status=status.HTTP_204_NO_CONTENT
            )


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    List all departments or create a new department
    """

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

