from django.db import models

class employee_data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    mobile_number = models.BigIntegerField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=20)


