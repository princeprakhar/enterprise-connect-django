

from django.http import HttpRequest,HttpResponse


def home(request:HttpRequest) -> HttpResponse:
  return HttpResponse("<h1>this is home page</h1>")