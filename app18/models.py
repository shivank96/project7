from django.db import models

class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.FloatField()

class EmployeeModels(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    password = models.CharField(max_length=100)

