from django.db import models

# Create your models here.
class Company(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Strickoff', 'Strickoff'),

    )
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    country = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    department = models.CharField(max_length=20)
    salary = models.FloatField()
    def __str__(self):
        return self.first_name