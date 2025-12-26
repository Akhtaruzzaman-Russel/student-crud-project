
from django.contrib import admin
from django.urls import path
from basic_project.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage, name="homePage" ),
    path('AddStudentPage/', AddStudentPage, name="AddStudentPage" ),
    path('StudentListPage/', StudentListPage, name="StudentListPage" ),
    path('EditStudentPage/<str:myid>', EditStudentPage, name="EditStudentPage" ),
    path('DeleteStudent/<str:myid>', DeleteStudent, name="DeleteStudent" ),
    path('UpdateStudent/', UpdateStudent, name="UpdateStudent" ),
    path('ViewStudent/<str:myid>', ViewStudent, name="ViewStudent" ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
