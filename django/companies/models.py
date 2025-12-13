from django.db import models

# empresa
class Enterprise(models.Model):
    name = models.CharField(max_length=180)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

# funcionario
class Employee(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)