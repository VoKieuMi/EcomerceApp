from django.contrib.auth.models import AbstractUser
from django.db import models
from oauth2_provider.models import Application


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
# Create your models here.
class User(AbstractUser):
    ROLE = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=20, choices=ROLE, default='user')

    avatar = models.ImageField(upload_to='images/avatar/%Y/%m/%d', null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Tên liên kết ngược khác
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Tên liên kết ngược khác
        blank=True
    )

    def __str__(self):
        return self.username

class StoreCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# Mô hình ProductCategory
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE, related_name='product_categories')

    def __str__(self):
        return self.name


# Mô hình Store
class Store(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stores')
    address = models.CharField(max_length=255)
    category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE, related_name='stores')

    def __str__(self):
        return self.name


# Mô hình Product
class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


# Model Review
class Review(BaseModel):
    rating = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    vendor = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='reviews')


    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"


# Model Order
class Order(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    payment = models.CharField(max_length=255)
    status_payment = models.CharField(max_length=255)


    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


# Model OrderItem
class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.product.name} in Order {self.order.id}"


# Model Transaction
class Transaction(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)


    def __str__(self):
        return f"Transaction {self.id} for Order {self.order.id}"


# Model SaleStatistics
class SaleStatistics(BaseModel):
    vendor = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='sale_statistics')
    month = models.IntegerField()
    quarter = models.IntegerField()
    year = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SaleStatistics {self.vendor.name} {self.month}/{self.year}"


# Model AdminStatistics
class AdminStatistics(BaseModel):
    vendor = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='admin_statistics')
    month = models.IntegerField()
    quarter = models.IntegerField()
    year = models.IntegerField()
    sold = models.IntegerField()
    total = models.IntegerField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AdminStatistics {self.vendor.name} {self.month}/{self.year}"