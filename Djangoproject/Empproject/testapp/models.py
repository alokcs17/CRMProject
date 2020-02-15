from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='companies', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'country')

    def __str__(self):
        return "%s (%s)" % (self.name, self.country)


class Department(models.Model):
    name = models.CharField(max_length=60)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'company')

    def __str__(self):
        return "%s (%s)" % (self.name, self.company)


class Degree(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'state')

    def __str__(self):
        return self.name


class Address(models.Model):
    address1 = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    police_station = models.CharField(max_length=50)
    pin_code = models.IntegerField()

    def __str__(self):
        return self.address1


class Employee(models.Model):
    number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    email = models.EmailField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    salary = models.FloatField()
    degree = models.ForeignKey(Degree,on_delete=models.CASCADE)
    pan = models.CharField(max_length=50)
    adhaar = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('number', 'company')

    def __str__(self):
        return self.first_name

    def __unicode__(self):
        return "{0}".format(self.first_name)
