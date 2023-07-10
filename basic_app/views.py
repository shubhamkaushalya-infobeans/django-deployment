from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.
def index(request):
    return render(request, 'basic_app/relative_template.html' )

def otherpage(request):
    return render(request, 'basic_app/other.html' )
    


