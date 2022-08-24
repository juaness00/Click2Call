from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,unique= True)
    password = models.CharField(max_length=255)
    userType = models.ForeignKey('UserType', on_delete=models.CASCADE)
    def __str__(self):
        return self.username
    def __int__(self):
        return self.userType
    
class Client(User):
    paymentMethod_id = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    contactInfo = models.EmailField()
    plan_id = models.ForeignKey('Plan', on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
   # payToken = models.CharField()
    def __str__(self):
        return self.name
    def __int__(self):
        return self.id
    

class Admin(User):
    clients = Client.objects.all

    

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    refreshRate = models.IntegerField()
    def __str__(self):
        return self.name
    def __int__(self):
        return self.id

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    color = models.IntegerField()
    #authorizedWebsites = 
    def __str__(self):
        return self.name
    def __int__(self):
        return self.id

class UserType(models.Model):
    name = models.CharField(max_length=255)
    isAllowedToModifyClients = models.BooleanField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
       return self.name
    def __int__(self):
        return self.id

class ProductWebsites(models.Model):
    name = models
    