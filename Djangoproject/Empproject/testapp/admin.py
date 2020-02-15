from django.contrib import admin
from .models import Employee,Company,Department,Country,City,State,Degree,Address

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_filter=['name']

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['name']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['number','first_name','last_name','phone_no','email',
                  'address','salary',
                  'degree','pan','adhaar','company','department']
    #list_display = ( 'get_degrees',)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address1','state','police_station','pin_code']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

class StateAdmin(admin.ModelAdmin):
    list_display = ['name']

class DegreeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Country)
admin.site.register(Address,AddressAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(Degree,DegreeAdmin)
