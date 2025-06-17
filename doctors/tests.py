from django.test import TestCase
from patients.models import Patient
from doctors.models import Doctor
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User, Group


class DoctorViewSetTests(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1996-08-24",
            contact_number="1234567890",
            email="john.doe@example.com",
            address="123 Main St, Anytown, USA",
            medical_history="No medical history",
        )
        self.doctor = Doctor.objects.create(
            first_name="Jane",
            last_name="Doe",
            qualification="MBBS",
            contact_number="1234567890",
            email="jane.doe@example.com",
            address="123 Main St, Anytown, USA",
            biography="No biography",
            is_on_vacation=False,
        )
        self.user = User.objects.create_user(
            username="jane.doe", email="jane.doe@example.com", password="testpass123"
        )
        self.doctors_group = Group.objects.create(name="doctors")
        self.user.groups.add(self.doctors_group)

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_should_return_200(self):
        url = reverse("doctor-appointments", kwargs={"pk": self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
