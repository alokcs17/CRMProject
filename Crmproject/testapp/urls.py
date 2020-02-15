from django.urls import path
from . import views
from testapp.views import EmployeeChartView


urlpatterns = [
    path('', views.home, name="home"),
    path('company/', views.company, name='company'),
    path('employee/', views.employee, name='employee'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
    path('bar_chart/', views.bar_chart, name='bar_chart'),
    #path('get/', EmployeeChartView.as_view(), name='get_context_data'),
    path('create_employee/', views.createEmployee, name='create_employee'),
    path('create_company/', views.createCompany, name='create_company'),
    path('update_company/<str:pk>/', views.updateCompany, name="update_company"),
    path('delete_company/<str:pk>/', views.deleteCompany, name="delete_company"),
    path('export/', views.export_users_xls, name='export_users_xls'),

]