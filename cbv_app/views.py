from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse

# Create your views here.

class Index(TemplateView):
    model = models.School
    # template_name = 'cbv_app/school_list.html'

class SchoolList(ListView):
     context_object_name = 'school_details'
     model = models.School

class SchoolDetail(DetailView):
     context_object_name = 'school_detail_view'
     model = models.School
     template_name = 'cbv_app/school_detail.html'

class CreateSchool(CreateView):
     model = models.School
     fields = ('name','principal','location')
     template_name = 'cbv_app/create.html'

     def get_success_url(self):
          return reverse('cbv_app_name:school-list')

class UpdateSchool(UpdateView):
     model = models.School
     fields = ('name','principal')
     template_name = 'cbv_app/create.html'
     def get_success_url(self):
          return reverse('cbv_app_name:school-list')
     
class DeleteSchool(DeleteView):
     model = models.School
     def get_success_url(self):
          return reverse('cbv_app_name:school-list')

          
     