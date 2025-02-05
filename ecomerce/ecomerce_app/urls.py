from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, StoreCategoryViewSet, ProductCategoryViewSet,
    StoreViewSet, ProductViewSet, ReviewViewSet, OrderViewSet,
    OrderItemViewSet, TransactionViewSet, SaleStatisticsViewSet,
    AdminStatisticsViewSet
)

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'store-categories', StoreCategoryViewSet, basename='store-category')
router.register(r'product-categories', ProductCategoryViewSet, basename='product-category')
router.register(r'stores', StoreViewSet, basename='store')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'reviews', ReviewViewSet, 'review')
router.register(r'orders', OrderViewSet, 'order')
router.register(r'order-items', OrderItemViewSet, 'order-item')
router.register(r'transactions', TransactionViewSet, 'transaction')
router.register(r'sale-statistics', SaleStatisticsViewSet, 'sale-statistic')
router.register(r'admin-statistics', AdminStatisticsViewSet)


urlpatterns = [
    path('', include(router.urls))

]

