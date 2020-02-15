from django.forms import Form
from django.shortcuts import render, redirect
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
import json

from .models import *
from .forms import *
from .filters import CompanyFilter
from django.views.generic import TemplateView
import xlwt
from django.http import HttpResponse

# Create your views here.
from .serialier import SnippetSerializer


def home(request):
    employees = Employee.objects.all()
    companys = Company.objects.all()
    total_company = companys.count()
    total_employees = employees.count()
    company_status = companys.filter(status='Active').count()
    salary_morethan = employees.filter(salary__gte=15000).count()
    salary_lessthan = employees.filter(salary__lt=15000).count()
    context = {'employees': employees, 'companys': companys, 'total_company': total_company,
               'total_employees': total_employees, 'company_status': company_status,
               'salary_morethan': salary_morethan, 'salary_lessthan': salary_lessthan}

    return render(request, 'testapp/dashboard.html', context)

def employee(request):
    employee = Employee.objects.all()
    return render(request, 'testapp/employee.html', {'employee': employee})

def createEmployee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'testapp/employee_form.html', context)

def company(request):
    company = Company.objects.all()
    #com = company.order_set.all()
    total_company = company.count()
    company_status = company.filter(status='Active').count()
    myFilter = CompanyFilter(request.GET, queryset=company)
    company = myFilter.qs
    context = {'myFilter':myFilter, 'company': company, 'total_company': total_company, 'company_status':
    company_status}
    return render(request, 'testapp/company.html', context)

def createCompany(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'testapp/company_form.html', context)

def updateCompany(request, pk):
    company = Company.objects.get(id=pk)
    form = CompanyForm(instance=company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'testapp/company_form.html', context)

def deleteCompany(request, pk):
    company = Company.objects.get(id=pk)
    if request.method == "POST":
        company.delete()
        return redirect('/')
    context = {'item': company}
    return render(request, 'testapp/delete.html', context)

def pie_chart(request):
    queryset = Company.objects.all()
    answers_list = []
    for col_num in queryset:
        dict = {}
        dict["label"] = col_num.name
        dict["value"] = 15
        answers_list.append(dict)
    content = json.dumps(answers_list)

    context = {"my_data": content}
    return render(request, 'testapp/graph.html', context)

def bar_chart(request):
    queryset = Employee.objects.all()
    answers_list = []
    for col_num in queryset:
        dict = {}
        dict["label"] = col_num.salary
        dict["value"] = col_num.salary
        answers_list.append(dict)
    content = json.dumps(answers_list)
    return render(request, 'testapp/charts.html', {"my_data": content})

class EmployeeChartView(TemplateView):
    template_name = 'testapp/charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Employee.objects.all()
        return context

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment ; filename="company.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Company')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Company Name', 'Phone Number', 'Email Id', 'Country Name', 'Status']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Company.objects.all().values_list('name', 'phone', 'email', 'country', 'status')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

