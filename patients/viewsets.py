from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    List all patients or create a new patient
    """

    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    @action(methods=["post"], detail=True, url_path="set-patient-declined")
    def set_patient_declined(self, request, pk):
        patient = self.get_object()
        patient.is_declined = True
        patient.save()
        return Response(
            {"message": "Patient is now declined", "status": status.HTTP_200_OK}
        )

    @action(methods=["post"], detail=True, url_path="set-patient-accepted")
    def set_patient_accepted(self, request, pk):
        patient = self.get_object()
        patient.is_declined = False
        patient.save()
        return Response(
            {"message": "Patient is now accepted", "status": status.HTTP_200_OK}
        )
