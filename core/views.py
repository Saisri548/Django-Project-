
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "application": "Django CI/CD Demo",
        "status": "healthy",
        "message": "My first Django application"
    })
