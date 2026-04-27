from django.db import models

class Mechanic(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    car_model = models.CharField(max_length=100)
    service_date = models.DateField()
    description = models.CharField(max_length=200)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car_model} - {self.service_date}"