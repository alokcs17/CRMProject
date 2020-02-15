from django.forms import ModelForm
from .models import *

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

