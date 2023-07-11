from django.urls import path
from . import views

app_name = 'cbv_app_name'
urlpatterns = [
    # modular routes for applicatin based
    # path('school-list/',views.Index.as_view(), name="school-list"),
    path('school-list/',views.SchoolList.as_view(), name="school-list"),
    path('school-detail/<int:pk>/',views.SchoolDetail.as_view(), name="school-details-page"),
    path('school-create/',views.CreateSchool.as_view(), name="school-create"),
    path('school-update/<int:pk>/',views.UpdateSchool.as_view(), name="school-update"),
    path('school-delete/<int:pk>/',views.DeleteSchool.as_view(), name="school-delete"),

]
