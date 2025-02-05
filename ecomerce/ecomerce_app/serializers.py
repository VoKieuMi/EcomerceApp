from rest_framework import serializers
from .models import (
    User, StoreCategory, ProductCategory, Store, Product,
    Review, Order, OrderItem, Transaction, SaleStatistics, AdminStatistics
)

from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # avatar = serializers.ImageField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email','password', 'role','is_superuser', 'is_active','avatar', 'date_joined']
        extra_kwargs ={
            'password': {'write_only': True},

            'is_active': {'read_only': True},
            'date_joined': {'read_only': True},
        }

    def create(self, validated_data):
        role = validated_data.get('role', 'user')  # Mặc định là người dùng

        # Nếu đăng ký là "seller", tài khoản sẽ cần xác nhận trước khi kích hoạt
        if role == ['user', 'admin', 'staff']:
            validated_data['is_superuser'] = True

        if role == 'seller':
            validated_data['is_active'] = False
            validated_data['is_superuser'] = False


        user = User.objects.create_user(**validated_data)
        return user


# StoreCategory Serializer
class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCategory
        fields = ['id', 'name', 'description']


# ProductCategory Serializer
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description', 'store_category']


# Store Serializer
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'owner', 'address', 'category', 'created_data', 'updated_data', 'active']


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'image', 'store', 'product_category', 'created_data', 'updated_data', 'active']


# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'user', 'product', 'vendor', 'created_data', 'updated_data', 'active']


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'total', 'status', 'payment', 'status_payment', 'created_data', 'updated_data', 'active']


# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price', 'created_data', 'updated_data', 'active']


# Transaction Serializer
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'order', 'payment_amount', 'payment_status', 'payment_method', 'created_data', 'updated_data', 'active']


# SaleStatistics Serializer
class SaleStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleStatistics
        fields = ['id', 'vendor', 'month', 'quarter', 'year', 'total', 'create', 'created_data', 'updated_data', 'active']


# AdminStatistics Serializer
class AdminStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminStatistics
        fields = ['id', 'vendor', 'month', 'quarter', 'year', 'sold', 'total', 'create', 'created_data', 'updated_data', 'active']
