from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CompanyViewSet, EmployeeViewSet


routers = DefaultRouter()

routers.register(r'companies', CompanyViewSet)
routers.register(r'employees', EmployeeViewSet)


urlpatterns = [
  path('', include(routers.urls)),
]
