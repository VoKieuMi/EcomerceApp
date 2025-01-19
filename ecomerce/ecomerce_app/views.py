from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import (
    User, StoreCategory, ProductCategory, Store, Product,
    Review, Order, OrderItem, Transaction, SaleStatistics, AdminStatistics
)
from .serializers import (
    UserSerializer, StoreCategorySerializer, ProductCategorySerializer,
    StoreSerializer, ProductSerializer, ReviewSerializer, OrderSerializer,
    OrderItemSerializer, TransactionSerializer, SaleStatisticsSerializer,
    AdminStatisticsSerializer
)

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# StoreCategory ViewSet
class StoreCategoryViewSet(viewsets.ModelViewSet):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer

# ProductCategory ViewSet
class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

# Store ViewSet
class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# OrderItem ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# Transaction ViewSet
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# SaleStatistics ViewSet
class SaleStatisticsViewSet(viewsets.ModelViewSet):
    queryset = SaleStatistics.objects.all()
    serializer_class = SaleStatisticsSerializer

# AdminStatistics ViewSet
class AdminStatisticsViewSet(viewsets.ModelViewSet):
    queryset = AdminStatistics.objects.all()
    serializer_class = AdminStatisticsSerializer
