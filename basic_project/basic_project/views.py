from django.shortcuts import render, redirect
from studentApp.models import StudentInfoModel


def homePage(request):
    return render(request, "homePage.html")


def AddStudentPage(request):
    if request.method=="POST":
        name=request.POST.get("sName")
        email=request.POST.get("sEmail")
        age=request.POST.get("sAge")
        course=request.POST.get("Course")
        address=request.POST.get("Address")

        studentdetails=StudentInfoModel(
            name=name,
            email=email,
            age=age,
            course=course,
            address=address,
        )
        studentdetails.save()

        return redirect("StudentListPage")
    return render(request, "AddStudentPage.html")



def StudentListPage(request):

    alldata=StudentInfoModel.objects.all()

    context={
        'studentdata':alldata
    }

    return render(request, "StudentListPage.html",context)


def EditStudentPage(request,myid):
    editstu=StudentInfoModel.objects.filter(id=myid)

    context={
        'edistudent':editstu
    }

    return render(request, "EditStudentPage.html",context)

def DeleteStudent(request,myid):
    deleteStd=StudentInfoModel.objects.get(id=myid)
    deleteStd.delete()

    return redirect("StudentListPage")

    # return render(request, "DeleteStudent")  



def UpdateStudent(request):
    if request.method=="POST":
        myid=request.POST.get('sID')
        name=request.POST.get('sName')
        email=request.POST.get('sEmail')
        age=request.POST.get('sAge')
        course=request.POST.get('Course')
        address=request.POST.get('Address')

        upStudent=StudentInfoModel(
            name=name,
            email=email,
            age=age,
            course=course,
            address=address,
        )
        upStudent.save()

    return redirect("StudentListPage.html")