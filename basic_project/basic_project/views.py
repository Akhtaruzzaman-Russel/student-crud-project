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
        image=request.FILES.get("Image")

        studentdetails=StudentInfoModel(
            name=name,
            email=email,
            age=age,
            course=course,
            address=address,
            image=image,
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
        PrevousImage=request.POST.get('PrevousImage')
        image=request.FILES.get("Image")

        if image:
            upStudent=StudentInfoModel(
            id=myid,
            name=name,
            email=email,
            age=age,
            course=course,
            address=address,
            image=image,
            )

        else:
            upStudent=StudentInfoModel(
            id=myid,
            name=name,
            email=email,
            age=age,
            course=course,
            address=address,
            image=PrevousImage,
            )
            upStudent.save()




        # upStudent=StudentInfoModel(
        #     id=myid,
        #     name=name,
        #     email=email,
        #     age=age,
        #     course=course,
        #     address=address,
        #     image=image,
        # )
        # upStudent.save()

    return redirect("StudentListPage")

def ViewStudent(request,myid):
    return render(request,"ViewStudent.html")