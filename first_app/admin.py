from django.contrib import admin
from first_app.models import Student, StudentBooks, Books, User, UserProfileMoreInformationForm

# Register your models here.
admin.site.register(Student)
admin.site.register(Books)
admin.site.register(StudentBooks)
admin.site.register(User)
admin.site.register(UserProfileMoreInformationForm)
