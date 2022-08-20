from django.contrib import admin
from .models import User, Client, PaymentMethod, Admin, Plan, Product, Usertype
# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(PaymentMethod)
admin.site.register(Admin)
admin.site.register(Plan)
admin.site.register(Product)
admin.site.register(Usertype)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','userType')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','paymentMethodId','productId','contactInfo','planId')

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id',)

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description','refreshRate')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','message','color',)
    
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name','isAllowedToModifyClients')