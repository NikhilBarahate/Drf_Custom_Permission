from django.shortcuts import render
from app1.models import Employee
from app1.serializers import EmployeeSerilaizer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from app1.permissions import IsReadonly, IsGetPostPut, RolePermissions

# Create your views here.
class EmployeeDetails(viewsets.ModelViewSet):
    serializer_class = EmployeeSerilaizer
    queryset = Employee.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [RolePermissions,]