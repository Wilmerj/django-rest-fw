from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer

class PatientSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "contact_number",
            "email",
            "address",
            "medical_history",
            "appointments",
        ]

    def validate(self, attrs):
        if "@example.com" not in attrs["email"]:
            raise serializers.ValidationError("Domain must contain @example.com")
        if attrs["is_declined"] == True and len(attrs["medical_history"]) > 0:
            raise serializers.ValidationError(
                "Patient cannot be declined without medical history"
            )
        return super().validate(attrs)


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"
