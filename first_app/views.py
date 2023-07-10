from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Student, StudentBooks, Books
from first_app import forms, signup, signup_auth_form
# for login
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    user_details = {'name':'shubham', 'last_name':'kaushalya'}
    student_details = Student.objects.order_by('id')
    student_data = {'student_record':student_details}
    # print(student_data)
    # return render(request, 'first_app/index.html', context=student_data)
    return render(request, 'first_app/index.html',{'name':'shubham', 'last_name':'kaushalya' ,'student_record':student_details})
    # return HttpResponse('stat')
    # return HttpResponse('Welcome shubham in django application')

def contactUs(request):
    form = forms.ContanctForm()

    if request.method == 'POST':
        # print('sfsd')
        form = forms.ContanctForm(request.POST)
        if form.is_valid():
            print('Data validation success')
            print('Name is: '+form.cleaned_data['name'])
            print('email is: '+form.cleaned_data['email'])
            print('gender is: '+form.cleaned_data['gender'])
            print('message is: '+form.cleaned_data['message'])

    return render(request, 'first_app/contact_form.html',{'form':form})

# Signup form using Modal type form 
def sign_up(request):
    signupform = signup.Signup()
    if request.method == 'POST':
        form = signup.Signup(request.POST)
        if  form.is_valid():
            form.save()
            return index(request)

    return render(request, 'first_app/signup.html',{"form":signupform})

def signup_auth(request):

    registered = False

    if request.method == 'POST':

        user_form = signup_auth_form.UserForm(data=request.POST)
        profile_form = signup_auth_form.UserProfileMoreInformationFormView(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            save_user = user_form.save()

            save_user.set_password(save_user.password)

            save_user.save()

            profile = profile_form.save(commit=False)

            profile.user =  save_user

            if 'profile_pic' in request.FILES:

                print('profile available')

                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

            print('ok')
        else: 
             print('fail')
             print(user_form.errors,profile_form.errors)

    else:

        user_form = signup_auth_form.UserForm()
        profile_form = signup_auth_form.UserProfileMoreInformationFormView()

    return render(request, 'first_app/signup_auth.html',{"user_form":user_form,"profile_form":profile_form,'registered':registered })


def login_auth(request):

    # return HttpResponseRedirect('/first_app/home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = authenticate(username=username, password=password)
        if user_obj:
             if user_obj.is_active:
                    test = login(request,user_obj)
                    # print('test---------------')
                    print(request.user.get_full_name())
                    return HttpResponseRedirect('/first_app/home')
                    # return HttpResponseRedirect(reverse('contact-page'))
             else:
                 return HttpResponse('You account is not activated yet')

        else:
            return HttpResponse('Something went wrong')
        
    else:
        return render(request, 'first_app/login.html',{})
    
def logout_call(request):
    logout(request)
    return HttpResponseRedirect('/first_app/home')