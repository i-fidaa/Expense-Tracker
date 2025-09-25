from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.amount}"
