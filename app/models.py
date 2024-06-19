from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images/')
    land = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name

