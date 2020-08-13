"""blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from user import views as user_views

urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('SignUp/',user_views.SignUp,name = "blog-SignUp"),
    path('Login/',user_views.Login,name = "blog-Login"),
    path('logout/',user_views.Logout,name = "user-logout"),
    path('Profile/',user_views.Profile,name = "Profile"),
    path('Profile/ChangeUsername',user_views.ChangeUsername,name = "ChangeUsername"),
    path('Profile/ChangeName',user_views.ChangeName,name="ChangeName"),
    path('Profile/ChangeEmail',user_views.ChangeEmail,name="ChangeEmail"),
    path('Profile/ChangePassword',user_views.ChangePassword,name="ChangePassword"),
]
