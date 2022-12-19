from django.db import models
from django.contrib.auth.models import User

#napisz modele od nowa bo sa totalnie zle zrobione

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} customer"



class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField()
    date_of_order = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.customer.username}'s order"


class ShippingAddress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    city = models.TextField()
    street = models.TextField()
    building_number = models.IntegerField()
    apartment_number = models.IntegerField()
    zipcode = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.customer.username}'s shipping info"


class OrderItem(models.Model):
    quantity = models.IntegerField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    #add __str__ for OrderItem


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.name}"




