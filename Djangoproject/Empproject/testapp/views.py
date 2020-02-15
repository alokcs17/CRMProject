from django.shortcuts import render
from .models import Employee,Department,City,Degree
from rest_framework import viewsets
from .serializer import EmployeeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max,Avg,Min


class EmployeeViewSet(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        if request.query_params.get('emp_first_name') is not None:
            name = request.query_params.get('emp_first_name')
            employees = employees.objects.filter(first_name=name)
        if request.query_params.get('department_name') is not None:
            name = request.query_params.get('department_name')
            department_ids = list(Department.objects.values_list('id', flat=True).filter(name=name))
            employees = employees.objects.filter(department_id__in=department_ids)
        if request.query_params.get('city_name') is not None:
            name = request.query_params.get('city_name')
            city = City.objects.filter(name=name)
            employees = employees.objects.filter(city__in=city)
        if request.query_params.get('degree_name') is not None:
            name = request.query_params.get('degree_name')
            degree = Degree.objects.filter(name=name)
            employees = employees.objects.filter(degree__in=degree)
        if request.query_params.get('min_salary') is not None:
            min_salary = request.query_params.get('min_salary')
            employees = employees.objects.filter(salary__gte=min_salary)
        if request.query_params.get('max_salary') is not None:
            max_salary = request.query_params.get('max_salary')
            employees = employees.objects.filter(salary__lte=max_salary)
        if request.query_params.get('top_n_salary') is not None:
            count = request.query_params.get('top_n_salary')
            employees = employees.objects.order_by('-salary')[0:count]
        serializer = EmployeeSerializer(employees,many=True)
        return Response(
            {
                'status': True,
                'message': "Successfully fetched",
                'data': serializer.data
            },
            status.HTTP_200_OK
        )

    def post(self, request):
        return print({'name': request.POST.get('first_name')})
        #return Response({'employee_department':request.POST.get('employee_department')})




#class CompanyViewSet(viewsets.ModelViewSet):
    #queryset = Company.objects.all()
    #serializer_class = Company


        '''elif request.query_params.get('employee_salary') is not None:
            salary= request.query_params.get('employee_salary')
            employees=Employee.objects.all().aggregate(Avg(salary))
            serializer=EmployeeSerializer(employees,many=True)
            return Response({'status': True, 'message': "Successfully fetched",
                             'data': serializer.data}, status.HTTP_200_OK)'''


    '''def get(self,request):
        if request.query_params.get('employee_salary') is not None:
            employees=Employee.objects.all().order_by('-employee_salary')[0:3]
            serializer=EmployeeSerializer(employees,many=True)
            return Response({'status':True,'message':"Successfully fetched",
                         'data':serializer.data},status.HTTP_200_OK)


        else:
            return Response({'status': False, 'message': "Failed",
                             }, status.HTTP_404_NOT_FOUND)'''






