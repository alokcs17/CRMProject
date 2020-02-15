import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CompanyFilter(django_filters.FilterSet):
	class Meta:
		model = Company
		fields = '__all__'
		exclude = ['email', 'phone']

