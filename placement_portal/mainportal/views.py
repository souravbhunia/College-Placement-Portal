from placement_portal.mainportal.models import Student
from django.shortcuts import render
from .forms import StudentProfile
# Create your views here.
from django.shortcuts import render

def home(request):
   
    return render(request,'home.html')


def login(request):
   
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def add_show(request):
    if request.method=='POST':
        fm=StudentProfile(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            im=fm.cleaned_data['id']
            pw=fm.cleaned_data['email']
            Hm=fm.cleaned_data['HS_marks']
            Cm=fm.cleaned_data['current_cgpa']
            CB=fm.cleaned_data['current_backlogs']
            reg=Student(name=nm,id=im,email=pw,HS_marks=Hm,current_cgpa=Cm,current_backlogs=CB)
            reg.save()
    else:
         fm=StudentProfile()
    return render(request,'mainportal/addandshow.html',{'form':fm})

