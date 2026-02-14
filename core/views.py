from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')