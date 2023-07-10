from django.urls import path, re_path
from basic_app import views 

#template tagging
app_name = 'basic_app'
urlpatterns = [
    # re_path(r'^$', views.index, name='index'),
    path('relative-url-template', views.index, name='relative-template'),
    path('other-page-template', views.otherpage, name='other-page-name'),
    # path('home/', home.index, name='home'),
]