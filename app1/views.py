from django.shortcuts import render,redirect

from app1.models import student_model
from app1.forms import student_form
def student_details(request):
    data=student_model.objects.all()
    content={
        "data":data
    }
    return render(request,'frontend_app1/home.html',content)
def  student_empty(request):
    form=student_form()
    if request.method=="POST":
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home101')
    else:
        form=student_form
        content={
            "form":form
        }
        return render(request,'frontend_app1/form.html',content)


