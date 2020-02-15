from rest_framework import serializers
from .models import Company, Employee
class SnippetSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return instance



class EmployeeSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    salary = serializers.FloatField()
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return instance