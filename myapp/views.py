from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from myapp.models import Info
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
# from myapp.models import Info



    
def index(request):
    return render(request,'index.html')


def navbar(request):
    return render(request,'navbar.html')
    

def Sign_in(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        ads = request.POST['ads1']
        city = request.POST['city']

        con = Info(Name=name,Email=email,Pass=password,Ads=ads,City=city)
        con.save()
    return render(request,'sign_in.html')

# def Profile(request):
#     return render(request,'profile.html')

def Login(request):
    if request.method=='POST':
        Username =request.POST["Name"]
        userpassword =request.POST["Password"]
        print(userpassword,Username)
        user = authenticate(request, username=Username, password=userpassword)
        if user is not None:
            login(request,user)
            return render(request,'profile.html')

    else:
        return render(request,'login.html')

def Logout(request):
    logout(request)
    return render(request,'index.html')

def Profile(request):
    info = Info.objects.all()
    context = {'blogs':info}
    return render(request,'profile.html',context)