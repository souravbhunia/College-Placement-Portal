from django.shortcuts import render

def home(request):
   
    return render(request,'home.html')


def login(request):
    get_button=request.GET.get('studentloginbutton','default')
    print(get_button)
    return render(request,'login_register.html')

