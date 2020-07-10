from django.shortcuts import render,redirect
from django.contrib.messages.views import SuccessMessageMixin
from  django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView,DeleteView,View
from  app18.models import EmployeeModel,EmployeeModels

# class ShowIndex(TemplateView):
#     template_name = "index.html"
class Add_employee(SuccessMessageMixin,CreateView):
    template_name = "emp_registration.html"
    model = EmployeeModels
    fields = "__all__"
    success_url = "/add_new/"
    success_message = "User details saved successfully"

class EmployeeInfo(ListView):
    template_name = "emp_info.html"
    model = EmployeeModels
    queryset = EmployeeModels.objects.values('name','idno')


class Update_info(UpdateView):
    template_name = "Update_emp_details.html"
    model = EmployeeModels
    fields = "__all__"
    success_url = '/view_employees/'


class ShowFullDetails(DetailView):
    template_name = "full_details.html"
    model = EmployeeModels


class DeleteEmployee(DeleteView):
    template_name = "confirm_delete_emp.html"
    model = EmployeeModels
    success_url = '/view_employees/'


def show_login(request):
    return render(request,"login.html")


def Check_credentials(request):
    uname = request.POST.get("uname")
    pwd = request.POST.get("pwd")
    result = EmployeeModels.objects.get(name=uname)
    if result.name == uname and result.password == pwd:
        return render(request, "home.html")
    else:
        return redirect('main')


class Viewall(View):
    pass