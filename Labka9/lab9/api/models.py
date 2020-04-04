from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default="")
    city = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default="")
    salary = models.FloatField()
    company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }

# Create your models here.
