from django.urls import path, re_path
from first_app import views 
from first_app.custom_views import home,class_base_views

#template tagging
app_name = 'first_app'
urlpatterns = [
    # re_path(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('home/', home.index, name='home'),
    path('signup-auth/', views.signup_auth, name='registration'),
    path('login-auth/', views.login_auth, name='login'),
    path('logout/', views.logout_call, name='logout'),
    path('cbv/',class_base_views.ClassBasedView.as_view())

]