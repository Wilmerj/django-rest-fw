from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet
from .viewsets import DepartmentViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = router.urls