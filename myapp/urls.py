from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navbar', views.navbar,name='navbar'),
    path('', views.index,name='index'),
    path('login/', views.Login,name='login'),
    path('sign_in/', views.Sign_in,name='sign_in'),
    path('profile', views.Profile,name='profile'),
    path('logout/', views.Logout,name='logout'),
]
