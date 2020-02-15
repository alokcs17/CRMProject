from rest_framework import serializers
from .models import Company, Employee, Country, Department, City, Degree, State


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    company = CompanySerializer()
    department = DepartmentSerializer()
    degree = DegreeSerializer()
    state = StateSerializer()
    city = CitySerializer()

    class Meta:
        model = Employee
        fields = '__all__'
        #depth = 3





'''class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model=Address
        fields='__all__'''





