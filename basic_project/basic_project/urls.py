
from django.contrib import admin
from django.urls import path
from basic_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage, name="homePage" ),
    path('AddStudentPage/', AddStudentPage, name="AddStudentPage" ),
    path('StudentListPage/', StudentListPage, name="StudentListPage" ),
    path('EditStudentPage/<str:myid>', EditStudentPage, name="EditStudentPage" ),
    path('DeleteStudent/<str:myid>', DeleteStudent, name="DeleteStudent" ),
    path('UpdateStudent/', UpdateStudent, name="UpdateStudent" ),
]
