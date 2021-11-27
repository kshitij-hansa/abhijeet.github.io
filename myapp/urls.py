from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navbar', views.navbar,name='navbar'),
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('Giriraj_bharat_Gas', views.Giriraj_bharat_Gas,name='Giriraj_bharat_Gas'),
]
