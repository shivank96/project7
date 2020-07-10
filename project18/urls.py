"""project18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from app18 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.ShowIndex.as_view(),name="main"),

    path('main/',TemplateView.as_view(template_name="index.html"),name="main"),

    path('add_new/',views.Add_employee.as_view(),name="add_new"),

    path('view_employees/',views.EmployeeInfo.as_view(),name="view_employees"),

    path('update_emp<int:pk>/',views.Update_info.as_view(),name="update_emp"),

    path('full_details<int:pk>/',views.ShowFullDetails.as_view(),name="full_details"),

    path('delete_emp<int:pk>/',views.DeleteEmployee.as_view(),name="delete_emp"),

    path('show/',views.show_login,name="show"),

    path('check/',views.Check_credentials,name="Check_Credentials"),

    path('viewall/',views.Viewall.as_view(),name="view")




]
