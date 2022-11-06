from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .ser import StudentSerializer

from .models import Student

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer