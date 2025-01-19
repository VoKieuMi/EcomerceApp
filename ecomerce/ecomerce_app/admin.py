from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'date_joined', 'email']

class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'store_category']
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description','owner','address','category']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','price','quantity','image','store','product_category']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['rating','comment','user','product','vendor']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','total','status','payment','status_payment']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity','price']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['order','payment_amount','payment_status','payment_method']


class SaleStatisticsAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'month', 'quarter', 'year', 'total']

class AdminStatisticsAdmin(admin.ModelAdmin):
    list_display = ['vendor','month','quarter','year','sold','total']


admin.site.register(User, UserAdmin)
admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(SaleStatistics, SaleStatisticsAdmin)
admin.site.register(AdminStatistics, AdminStatisticsAdmin)
