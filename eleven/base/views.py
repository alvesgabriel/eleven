# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'base/index.html')
    # return HttpResponse('Hello World')
