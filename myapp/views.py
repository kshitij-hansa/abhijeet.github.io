from django.shortcuts import render
from django.shortcuts import HttpResponse
from myapp.models import Info


    
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        ads = request.POST['ads1']
        city = request.POST['city']
        con = Info(Name=name,Email=email,Pass=password,Ads=ads,City=city)
        con.save()
    return render(request,'login.html')
    
def navbar(request):
    return render(request,'navbar.html')
    
def Giriraj_bharat_Gas(request):
    return render(request,'Giriraj_bharat_Gas.html')


    