from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CompanyViewSet


routers = DefaultRouter()

routers.register(r'companies', CompanyViewSet)


urlpatterns = [
  path('', include(routers.urls)),
]
