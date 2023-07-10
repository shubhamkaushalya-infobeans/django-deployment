from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {'name':'shubham kaushalya','number': 20}
    return render(request, 'first_app/home.html',context=data)
    # return HttpResponse('Welcome shubham in django home page within folder')

# Create your views here.
