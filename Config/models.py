from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255,unique= True)
    #passwordToken = models.charField()
    userType = models.ForeignKey('UserType', on_delete=models.CASCADE)
    def __int__(self):
        return self.userType
    
class Client(models.Model):
    user = models.ForeignKey('User',on_delete= models.CASCADE)
    paymentMethodId = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE)
    productId = models.ForeignKey('Product', on_delete=models.CASCADE)
    contactInfo = models.EmailField()
    planId = models.ForeignKey('Plan', on_delete=models.CASCADE)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)
   # payToken = models.CharField()
    def __str__(self):
        return self.name 

class Admin(models.Model):
    userType = models.ForeignKey('UserType',on_delete= models.CASCADE)
    

class Plan(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    refreshRate = models.IntegerField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    color = models.IntegerField()
    #authorizedWebsites = 
    def __str__(self):
        return self.name

class UserType(models.Model):
    name = models.CharField(max_length=255)
    isAllowedToModifyClients = models.BooleanField()
    id = models.AutoField(primary_key=True)

    #def __str__(self):
     #   return self.name

    def __int__(self):
        return self.id

class ProductWebsites(models.Model):
    name = models
    