from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Carts(models.Model):
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Movies,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.buyer}-->{self.item}'
    



