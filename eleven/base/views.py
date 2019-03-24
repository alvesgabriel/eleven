# Create your views here.
from django.http import HttpResponse


def home(request):
    # return render(request, 'Hello World')
    return HttpResponse('Hello World')
