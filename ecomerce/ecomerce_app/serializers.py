from rest_framework import serializers
from .models import (
    User, StoreCategory, ProductCategory, Store, Product,
    Review, Order, OrderItem, Transaction, SaleStatistics, AdminStatistics
)

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active', 'date_joined']
        # extra_kwargs ={
        #     'password': {
        #         'write_only': True
        #     },
        #     'role': {
        #         'write_only': True
        #     }
        # }


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
