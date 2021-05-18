"""Logo_Type_Identification_System URL Configuration

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
from os import name
from django.contrib import admin
from django.urls import path
from app import views
#For accessing static files we need to import
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


admin.site.site_header="Admin Panel"
admin.site.site_title="Admin Panel"

urlpatterns = [
     path('',views.home),
     path('', views.home , name=''),
     path('LogoType', views.LogoType , name='Logo Type'),
     path('ContactUs', views.ContactUs , name='Contact Us'),
     path('AboutUs.html', views.AboutUs , name='About Us'),
     path('LoginAndSignUp', views.LoginAndSignUp , name='Login And Sign Up'),
     path('userDashboard',views.userDashboard, name="userDashboard"),
     #Path for chat application
     path('Readmore.html',views.Readmore,name="Readmore"),
     path('userProfile',views.userprofile,name="userprofile"), 
     path('updateuser',views.updateuser,name="updateuser"),
     path('predictimage',views.predictimage,name="predictimage"),    
     path('AdminLogin',views.admin, name="AdminLogin"),   
     path('adminHome',views.adminHome, name="adminHome"),
     path('admin_profile',views.adminprofile,name='admin_profile'),
     path('updateAdmin',views.updateadmin,name='updateAdmin'),
     path('usersTable',views.userstable,name='usersTable'),
     path('contactusMessages',views.contactus_table_admin,name='contactusMessages'),
     path('userReview',views.userReview,name='userReview'),
     path('imagesuploadedAndTested',views.imagesuploadedAndTested,name='imagesuploadedAndTested'),

     
]


#For loading our images we have to include following url pattern FOR DEVELOPEMENT PURPOSE WE HAVE TO CHANGE IN 
#WHEN MAKING OUR WEB LIVE
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)